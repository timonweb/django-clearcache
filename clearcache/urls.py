from django.conf.urls import url
from .views import ClearCacheAdminView

urlpatterns = [
    url(r'$', ClearCacheAdminView.as_view(), name="clearcache_admin"),
]
