import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_profile_registration_view(client):
    url = reverse('registration')
    content = client.get(url)
    data = {
        'email': 'test@test.com',
        'fname': 'test',
        'lname': 'django',
        'password1': 'RanDom@123#',
        'password2': 'RanDom@123#',
        'mobile': '1234567890'
    }
    response = client.post(url, data=data)
    assert content.status_code == 200
    assert content.templates[0].name == 'profiles/registration.html'
    assert response.status_code == 200
