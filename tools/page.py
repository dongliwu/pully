#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : restful.py
# @Author: LiWu Dong
# @Date  : 2018/10/19
# @Email  : i@dongliwu.com


class Page():
    '''
        Page: 用于分页
    '''
    def __init__(self, page, limit):
        self.page = page
        self.limit = limit
    
    @property
    def start(self):
        '''
            start: 获得起始数
        '''
        return (self.page - 1) * self.limit
    
    @property    
    def end(self):
        '''
            end: 获得结束数
        '''
        return self.page * self.limit
