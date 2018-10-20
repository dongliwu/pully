#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : restful.py
# @Author: LiWu Dong
# @Date  : 2018/10/19
# @Email  : i@dongliwu.com

from __future__ import unicode_literals
from django.shortcuts import render

def idc_list(request):
    return render(request, 'asset/idcList.html')

def idc_add(request):
    return render(request, 'asset/idcAdd.html')

def idc_detail(request):
    return render(request, 'asset/idcDetail.html')

def idc_edit(request):
    return render(request, 'asset/idcEdit.html')

def idc_del(request):
    return render(request, 'asset/idcEdit.html')