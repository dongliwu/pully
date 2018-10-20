#/usr/bin/env python
#coding:utf-8
##################################
#Author: LiWu Dong               #
#Email : liwu.dong@deepcam.com   #
##################################

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from puser import urls as user_urls
from passet import urls as asset_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include(user_urls)),
    url(r'^assets/', include(asset_urls)),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
