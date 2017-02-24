import pytest

pytestmark = pytest.mark.django_db


def test_urls(client):
    urls = ['/admin', '']
    for url in urls:
        status = client.get(url)
        assert status.status_code == 200
