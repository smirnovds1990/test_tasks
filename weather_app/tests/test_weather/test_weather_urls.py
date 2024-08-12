from http import HTTPStatus

from django.urls import reverse


def test_index_is_reachable_for_all(client, admin_client):
    url_reverse = 'weather:index'
    url = reverse(url_reverse)
    non_auth_response = client.get(url)
    auth_response = admin_client.get(url)
    assert non_auth_response.status_code == HTTPStatus.OK
    assert auth_response.status_code == HTTPStatus.OK


def test_city_url(client, admin_client):
    url_reverse = 'weather:city'
    url = reverse(url_reverse, kwargs={'city': 'test_city'})
    non_auth_response = client.get(url)
    auth_response = admin_client.get(url)
    assert non_auth_response.status_code == HTTPStatus.FOUND
    assert auth_response.status_code == HTTPStatus.OK


def test_statistics_url(client, admin_client):
    url_reverse = 'weather:statistics'
    url = reverse(url_reverse)
    non_auth_response = client.get(url)
    auth_response = admin_client.get(url)
    assert non_auth_response.status_code == HTTPStatus.FOUND
    assert auth_response.status_code == HTTPStatus.OK
