import time

import pytest
from django.core.cache import cache
from django.core.management import call_command
from django.urls import reverse

CACHE_KEY = 'example_cache_key'
CACHE_VALUE = 'example_cache_value'


def test_cache_works():
    CACHE_EXPIRE_IN_SEC = 1

    assert cache.get(CACHE_KEY) is None, "The value isn't cached yet"

    cache.set(CACHE_KEY, CACHE_VALUE, CACHE_EXPIRE_IN_SEC)
    assert cache.get(CACHE_KEY) == CACHE_VALUE, "The value came from a cache"

    time.sleep(1)
    assert cache.get(CACHE_KEY) is None, "The value isn't cached because it's expired"


def test_clears_cache_via_command_line():
    cache.set(CACHE_KEY, CACHE_VALUE, 100)
    assert cache.get(CACHE_KEY) == CACHE_VALUE, "Cache populated"

    call_command('clearcache')

    assert cache.get(CACHE_KEY) is None, "Cache cleared"


@pytest.mark.django_db
def test_clear_cache_is_in_admin_index(admin_client):
    response = admin_client.get('/admin/')
    assert "Clear cache" in str(response.content)


@pytest.mark.django_db
def test_clear_cache_form_is_rendered(admin_client):
    response = admin_client.get(reverse('clearcache_admin'))
    assert "Clear cache now" in str(response.content), "Clear cache now button is visible"


@pytest.mark.django_db
def test_non_superuser_cant_access_clearcache(client):
    response = client.get(reverse('clearcache_admin'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_clears_cache_via_admin_ui(admin_client):
    cache.set(CACHE_KEY, CACHE_VALUE, 100)
    assert cache.get(CACHE_KEY) == CACHE_VALUE, "Cache populated"

    admin_client.post(reverse('clearcache_admin'), {
        'cache_name': 'default'
    })

    assert cache.get(CACHE_KEY) is None, "Cache cleared"
