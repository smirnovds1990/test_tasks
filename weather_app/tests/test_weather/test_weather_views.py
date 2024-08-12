from http import HTTPStatus

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_get_weather_page(admin_client):
    city = 'kineshma'
    template = 'weather/city.html'
    url_reverse = 'weather:city'
    url = reverse(url_reverse, kwargs={'city': city})
    response = admin_client.post(url)
    assert response.status_code == HTTPStatus.OK
    assert 'weather_info' in response.context
    assert 'city' in response.context
    assertTemplateUsed(response, template)


def test_get_statistics(admin_client):
    template = 'weather/statistics.html'
    url_reverse = 'weather:statistics'
    url = reverse(url_reverse)
    response = admin_client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert 'current_user_cities' in response.context
    assert 'all_cities' in response.context
    assertTemplateUsed(response, template)
