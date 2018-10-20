#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : restful.py
# @Author: LiWu Dong
# @Date  : 2018/10/19
# @Email  : i@dongliwu.com
##################################

from __future__ import unicode_literals
from passet.models import *  
from django.http.response import JsonResponse
from django.db.models import Q
from tools import page, common, restful

# 获取所有IDC信息
def idc_list(request):
    '''
        get idc list
    '''
    response = {}
    response['code'] = 0
    response['msg'] = ""
    search = request.GET.get('search', None)
    page_num = common.verify_int(request.GET.get('page', 1), 1)
    limit = common.verify_int(request.GET.get('limit', 14), 14)
    
    pageX = page.Page(page_num, limit)
    start = pageX.start
    end = pageX.end
    
    if search:
        querySet = IDC.objects.filter(Q(name__contains=search) | Q(provider__contains=search)).values('id','name','region','provider','address','contacts__name','contacts__phone','contract__end_date')[page.start:page.end]
        response['count'] = querySet.count()
    else:
        querySet = IDC.objects.values('id','name','region','provider','address','contacts__name','contacts__phone','contract__end_date')[start:end]
        response['count'] = IDC.objects.count()
    response['msg'] = "success"
    response['data'] = list(querySet)
    for item in range(len(response['data'])):
        response['data'][item]['contract__end_date'] = str(response['data'][item]['contract__end_date']).split(' ')[0]
    return JsonResponse(response)

#
def idc_detail(request):
    response = {}
    response['code'] = 0
    response['msg'] = ""
    return response

def idc_add(request):
    response = {}
    response['code'] = 0
    response['msg'] = ""
    return response

def idc_update(request):
    response = {}
    response['code'] = 0
    response['msg'] = ""
    return response

def idc_del(request):
    response = {}
    response['code'] = 0
    response['msg'] = ""
    id = request.POST.get('id', None)
    ids = request.POST.getlist('ids[]', None)
    if id:
        if IDC.objects.filter(id=id).delete():
            response['msg'] = "success"
        else:
            response['code'] = 1001
            response['msg'] = "no such id"
    elif ids:
        for id in ids:
            IDC.objects.filter(id=id).delete()
        response['msg'] = "success"
    else:
        response['code'] = 1002
        response['msg'] = "missing parameter"
    return response


def idc(request):
    response = restful.restful(request, idc_detail, idc_add, idc_update, idc_del)
    return JsonResponse(response)