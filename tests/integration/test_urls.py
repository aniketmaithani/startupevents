import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_urls(client):
    endpoints = ['home', 'registration']
    for endpoint in endpoints:
        url = reverse(endpoint)
        status = client.get(url)
        assert status.status_code == 200
