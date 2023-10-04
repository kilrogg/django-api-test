from django.contrib import admin
from django.urls import path, include
from django.views import debug

from .api import api_v1

admin.autodiscover()

urlpatterns = [
    path("", debug.default_urlconf),
    path('microsoft/', include('microsoft_auth.urls', namespace='microsoft')),
    path("admin/", admin.site.urls),
    path("api/v1/", api_v1.urls),
]
