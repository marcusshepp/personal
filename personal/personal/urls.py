from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from main.views import (
    Main,
    foo,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Main.as_view(), name="main"),
    url(r'^foo/$', foo, name="foo"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
