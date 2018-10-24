#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : input.py
# @Author: LiWu Dong
# @Date  : 2018/10/24
# @Email  : i@dongliwu.com

from django.http import QueryDict

def getData(request, field, default=None):
    '''
    :param request: 传入的请求
    :param field: 所需要返回值的字段
    :param default: 默认字段值
    :return: 返回字段值
    '''

    value = request.GET.get(field, None)
    if value is None:
        if default is None:
            return None
        else:
            return default
    else:
        return value

def getPostData(request, field, default=None):
    '''
    :param request: 传入的请求
    :param field: 所需要返回值的字段
    :param default: 默认字段值
    :return: 返回字段值
    '''

    value = request.POST.get(field, None)
    if value is None:
        if default is None:
            return None
        else:
            return default
    else:
        return value

def getQueryDict(request):
    '''
    :param request: 传入的请求
    :return: 返回请求体
    '''

    body = QueryDict(request.body)
    return body

def getRequestData(body, field, default=None):
    '''
    :param body: 请求体
    :param field: 所需要返回值的字段
    :param default: 默认字段值
    :return: 返回字段值
    '''

    value = body.get(field, None)
    if value is None:
        if default is None:
            return None
        else:
            return default
    else:
        return value
