#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : restful.py
# @Author: LiWu Dong
# @Date  : 2018/10/19
# @Email  : i@dongliwu.com

from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect

def login(request):
    data = {'msg':''}
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                data['msg'] = '用户已禁用!'
        else:
            data['msg'] = '用户名或密码错误!'
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'user/login.html',data)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))

def forgetPasswd(request):
    return render(request, 'ok')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username',None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        user = User.objects.create_user(username, email, password)
        user.save()
        return render(request, 'ok')
        
    else:
        return render(request, 'user/register.html')

 
@login_required(login_url='/users/login/')
def dashboard(request):
    data = {}
    return render(request, 'user/dashboard.html', data)
