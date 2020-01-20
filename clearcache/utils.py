from django.core.cache import caches


def clear_cache(cache_name):
    caches[cache_name].clear()
