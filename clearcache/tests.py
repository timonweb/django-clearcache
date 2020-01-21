import time

from django.core.cache import cache
from django.core.management import call_command

CACHE_KEY = 'example_cache_key'
CACHE_VALUE = 'example_cache_value'


def test_cache_works():
    CACHE_EXPIRE_IN_SEC = 1

    assert cache.get(CACHE_KEY) is None, "The value isn't cached yet"

    cache.set(CACHE_KEY, CACHE_VALUE, CACHE_EXPIRE_IN_SEC)
    assert cache.get(CACHE_KEY) == CACHE_VALUE, "The value came from a cache"

    time.sleep(1)
    assert cache.get(CACHE_KEY) is None, "The value isn't cached because it's expired"


def test_clears_cache():
    cache.set(CACHE_KEY, CACHE_VALUE, 100)
    assert cache.get(CACHE_KEY) == CACHE_VALUE, "Cache populated"

    call_command('clearcache')

    assert cache.get(CACHE_KEY) is None, "Cache cleared"
