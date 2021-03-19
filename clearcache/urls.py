from django.urls import path
from .views import ClearCacheAdminView

urlpatterns = [
    path('', ClearCacheAdminView.as_view(), name="clearcache_admin"),
]
