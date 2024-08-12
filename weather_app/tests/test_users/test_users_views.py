import pytest
from django.urls import reverse
from pytest_django.asserts import assertRedirects

from weather.models import User


@pytest.mark.django_db
def test_signupview(client):
    url_reverse = 'users:signup'
    data = {
        'username': 'test_user',
        'email': 'test_email@mail.ru',
        'password1': 'TestPassword123',
        'password2': 'TestPassword123'
    }
    url = reverse(url_reverse)
    response = client.post(url, data=data)
    users = User.objects.all()
    assert len(users) == 1
    assert users[0].username == 'test_user'
    assert users[0].email == 'test_email@mail.ru'
    assertRedirects(response, reverse('weather:index'))
