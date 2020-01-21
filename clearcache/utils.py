from django.conf import settings
from django.core.cache import caches


def clear_cache(cache_name):
    assert settings.CACHES
    caches[cache_name].clear()
