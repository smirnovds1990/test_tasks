from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import City
from .utils import (
    convert_data_to_dataframe, get_city_coordinates, get_weather_info,
    save_city_to_db
)


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            return redirect(reverse('weather:city', kwargs={'city': city}))
    return render(request, 'weather/index.html')


@login_required
def get_weather_page(request: HttpRequest, city: str) -> HttpResponse:
    latitude, longitude = get_city_coordinates(city)
    weather_info = get_weather_info(latitude, longitude)
    dataframed_weather_info = convert_data_to_dataframe(weather_info)
    save_city_to_db(city, request.user)
    return render(
        request,
        'weather/city.html',
        context={'weather_info': dataframed_weather_info, 'city': city}
    )


@login_required
def get_statistics(request: HttpRequest):
    current_user = request.user
    current_user_cities = current_user.cities.values('city_title').annotate(
        count=Count('city_title')
    ).order_by('-count')
    all_cities = City.objects.values('city_title').annotate(
        count=Count('city_title')
    ).order_by('-count')
    return render(
        request,
        'weather/statistics.html',
        context={
            'current_user_cities': current_user_cities,
            'all_cities': all_cities
        }
    )
