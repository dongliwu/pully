#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : restful.py
# @Author: LiWu Dong
# @Date  : 2018/10/19
# @Email  : i@dongliwu.com

from django.conf.urls import url
from passet import views as asset_views
from passet.api import idc as asset_api_idc

# api url
urlpatterns = [
    url(r'^api/idc/list', asset_api_idc.idc_list, name='idc_list'),
    url(r'^api/idc/', asset_api_idc.idc, name='idc'),
] 

# views url
urlpatterns += [
    url(r'^idc/list', asset_views.idc_list, name='idcList'),
    url(r'^idc/add/', asset_views.idc_add, name='idcAdd'),
    url(r'^idc/detail$', asset_views.idc_detail, name='idcDetail'),
    
]
