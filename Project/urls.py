
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from Main import urls
import os
from Project.settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(urls)),
    path('contact/',include('contact.urls'))
]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)