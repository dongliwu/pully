#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : restful.py
# @Author: LiWu Dong
# @Date  : 2018/10/19
# @Email  : i@dongliwu.com

from django import forms

# 用户表单
class UserForms(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    email = forms.EmailField()
    
