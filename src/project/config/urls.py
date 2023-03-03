from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config import settings
from menu import urls as menu_urls

urlpatterns = [
    path("", include(menu_urls)),
    path("admin/", admin.site.urls),
]

# for access to static files of admin panels in a docker container
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
