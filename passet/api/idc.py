#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : restful.py
# @Author: LiWu Dong
# @Date  : 2018/10/19
# @Email  : i@dongliwu.com
##################################

from __future__ import unicode_literals
from django.http import QueryDict
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
        querySet = IDC.objects.filter(Q(name__contains=search) | Q(provider__contains=search)).values('id', 'name', 'region', 'provider', 'address', 'contacts__name', 'contacts__phone', 'contracts__end_date')[start:end]
        response['count'] = querySet.count()
    else:
        querySet = IDC.objects.values('id', 'name', 'region', 'provider', 'address', 'contacts__name', 'contacts__phone', 'contracts__end_date')[start:end]
        response['count'] = IDC.objects.count()
    response['msg'] = "success"
    response['data'] = list(querySet)
    for item in range(len(response['data'])):
        response['data'][item]['contracts__end_date'] = str(response['data'][item]['contracts__end_date'])
    return JsonResponse(response)

#
def idc_detail(request):
    response = {}
    response['code'] = 0
    response['msg'] = ""
    return response

def idc_add(request):
    # TODO: make sure value is not None
    response = {}
    response['code'] = 0
    response['msg'] = ""
    name = request.POST.get('name', None)
    region = request.POST.get('region', None)
    provider = request.POST.get('provider', None)
    address = request.POST.get('address', None)
    if request.POST.get('contacts_id', None) is None:
        contacts_name = request.POST.get('contacts_name', None)
        contacts_email = request.POST.get('contacts_email', None)
        contacts_phone = request.POST.get('contacts_phone', None)
        contacts_obj = Contacts.objects.create(name=contacts_name, email=contacts_email, phone=contacts_phone)
    else:
        contacts_obj = Contacts.objects.filter(id=request.POST.get('contacts_id'))

    contacts = contacts_obj

    if request.POST.get('contracts_id', None) is None:
        contracts_sn = request.POST.get('contracts_sn', None)
        contracts_company = request.POST.get('contracts_company', None)
        contracts_staff = request.POST.get('contracts_staff', None)
        contracts_phone = request.POST.get('contracts_phone', None)
        contracts_title = request.POST.get('contracts_title', None)
        contracts_cost = request.POST.get('contracts_cost', None)
        contracts_start_date = request.POST.get('contracts_start_date', None)
        contracts_end_date = request.POST.get('contracts_end_date', None)
        contracts_abstract = request.POST.get('contracts_abstract', None)

        contracts_file = request.FILES.get('contracts_file', None)
        contracts_file_name = contracts_file.name
        contracts_file_path = "test"
        contracts_obj = Contracts.objects.create(sn=contracts_sn, company=contracts_company, staff=contracts_staff, phone=contracts_phone, title=contracts_title, cost=contracts_cost, start_date=contracts_start_date, end_date=contracts_end_date,abstract=contracts_abstract, file_name=contracts_file_name, file_path=contracts_file_path)
    else:
        contracts_obj = Contracts.objects.filter(id=request.POST.get('contracts_id'))

    contracts = contracts_obj

    IDC.objects.create(name=name, region=region, provider=provider, address=address, contacts=contacts, contracts=contracts)


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