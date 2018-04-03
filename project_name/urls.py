#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(r'admin/', admin.site.urls),
]

if settings.DEBUG:
    
    import debug_toolbar
    
    urlpatterns = [
        path(r'admin/doc/', include('django.contrib.admindocs.urls')),
        path(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
