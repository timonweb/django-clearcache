"""
    Test clearcache with regular user
"""

import pytest
from django.contrib.auth.models import Permission
from django.core.cache import cache
from django.urls import reverse

CACHE_KEY = 'example_cache_key'
CACHE_VALUE = 'example_cache_value'
CACHE_EXPIRE_IN_SEC = 1


@pytest.fixture
def regular_user_no_permission(db, django_user_model, django_username_field):
    user = django_user_model.objects.create_user(
        **{django_username_field: "username_no_perm",
           'password': "xxx"})
    user.is_staff = True  # To access Admin
    user.save()
    return user


@pytest.fixture
def regular_user_with_permission(db, django_user_model, django_username_field):
    user = django_user_model.objects.create_user(**{django_username_field: "username_with_perm",
                                                     'password': "xxx"})
    permission = Permission.objects.get(codename="use_clearcache")
    user.user_permissions.add(permission)
    user.is_staff = True
    user.save()
    return user



@pytest.mark.django_db
def test_clear_cache_in_admin_index(client,
                                    regular_user_no_permission,
                                    regular_user_with_permission):
    client.force_login(regular_user_no_permission)
    response = client.get('/admin/')
    assert response.status_code == 200
    assert "Clear cache" not in str(response.content)
    client.force_login(regular_user_with_permission)
    assert response.status_code == 200
    response = client.get('/admin/')
    assert "Clear cache" in str(response.content)


@pytest.mark.django_db
def test_clear_access_to_clearcache_form(client,
                                         regular_user_no_permission,
                                         regular_user_with_permission):
    url = reverse('clearcache_admin')
    client.force_login(regular_user_no_permission)
    response = client.get(url)
    assert response.status_code in [403, 302]
    client.force_login(regular_user_with_permission)
    response = client.get(url)
    assert response.status_code == 200
    assert "Clear cache now" in str(response.content), "Clear cache now button is visible"


@pytest.mark.django_db
def test_clears_cache_via_admin_ui(client,
                                   regular_user_no_permission,
                                   regular_user_with_permission):
    cache.set(CACHE_KEY, CACHE_VALUE, 100)
    assert cache.get(CACHE_KEY) == CACHE_VALUE, "Cache populated"
    client.force_login(regular_user_no_permission)
    client.post(reverse('clearcache_admin'), {
        'cache_name': 'default'
    })
    assert cache.get(CACHE_KEY) ==  CACHE_VALUE, "Cache not cleared"
    client.force_login(regular_user_with_permission)
    client.post(reverse('clearcache_admin'), {
        'cache_name': 'default'
    })
    assert cache.get(CACHE_KEY) is None, "Cache cleared"
