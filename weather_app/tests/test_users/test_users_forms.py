from django.urls import reverse

from users.forms import CreationForm


def test_creation_form(client):
    url_reverse = 'users:signup'
    url = reverse(url_reverse)
    response = client.get(url)
    assert 'form' in response.context
    assert isinstance(response.context['form'], CreationForm)
