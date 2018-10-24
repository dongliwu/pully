#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : restful.py
# @Author: LiWu Dong
# @Date  : 2018/10/19
# @Email  : i@dongliwu.com

from django.http import QueryDict

def restful(request, get=None, post=None, put=None, delete=None):
    '''
        restful: http请求restful化
        request: 通过http传递的请求
        get: 获取数据的函数
        post: 添加数据的函数
        put: 更新数据的函数
        delete: 删除数据的函数
    '''

    method = request.method
    response = []

    print(method)
    if method == 'GET':
        if get is None:
            response['code'] = 2001
            response['msg'] = "missing parameters"
        else:
            response = get(request)
        return response
    elif method == 'POST':
        if post is None:
            response['code'] = 2002
            response['msg'] = "missing parameters"
        else:
            response = post(request)
        return response
    elif method == 'PUT':
        if put is None:
            response['code'] = 2003
            response['msg'] = "missing parameters"
        else:
            response = put(request)
        return response
    elif method == 'DELETE':
        if delete is None:
            response['code'] = 2004
            response['msg'] = "missing parameters"
        else:
            response = delete(request)
        return response
    else:
        response['code'] = 2005
        response['msg'] = "missing parameters"
        return response
