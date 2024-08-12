from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.parametrize(
        'url_reverse',
        ('users:signup', 'users:login')
)
def test_anonymos_users_can_get_entry_urls(client, url_reverse):
    url = reverse(url_reverse)
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_anonymus_users_cant_get_logout_url(client):
    logout_reverse = 'users:logout'
    url = reverse(logout_reverse)
    response = client.get(url)
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
