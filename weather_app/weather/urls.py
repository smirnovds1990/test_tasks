from django.urls import path

from . import views


app_name = 'weather'

urlpatterns = [
    path('', views.index, name='index'),
    path('statistics/', views.get_statistics, name='statistics'),
    path('<city>/', views.get_weather_page, name='city'),
]
