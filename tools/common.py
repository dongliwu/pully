#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : common.py
# @Author: LiWu Dong
# @Date  : 2018/10/19
# @Email  : i@dongliwu.com

def verify_int(number, isNotNum = 1):
    '''
        number:需要被检测是否为数字的参数
        isNotNum:当number为非数字时返回的参数
    '''
    try :
        number = int(number)
    except TypeError:
        number = isNotNum
    return number
