#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : restful.py
# @Author: LiWu Dong
# @Date  : 2018/10/19
# @Email  : i@dongliwu.com

from django.conf.urls import include, url
from django.contrib import admin
from puser import views as user_views

urlpatterns = [
    url(r'^login/', user_views.login, name='login'),
    url(r'^dashboard/', user_views.dashboard, name='dashboard'),
    url(r'^logout/', user_views.logout, name='logout'),
    url(r'^forgetPasswd/', user_views.forgetPasswd, name='forgetPasswd'),
    url(r'^register/', user_views.register, name='register'),
]
