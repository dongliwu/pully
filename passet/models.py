#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : restful.py
# @Author: LiWu Dong
# @Date  : 2018/10/19
# @Email  : i@dongliwu.com

from __future__ import unicode_literals
from django.db import models

# 资产管理者信息
class Manager(models.Model):
    name = models.CharField(max_length=25, verbose_name=u'姓名')
    email = models.EmailField(max_length=25, null=True, blank=True, verbose_name=u'邮箱')
    phone = models.CharField(max_length=16, null=True, blank=True, verbose_name=u'电话')
    company = models.CharField(max_length=25, null=True, blank=True, verbose_name=u'所属公司')

    class Meta:
        verbose_name = u'资产管理员表'
        verbose_name_plural= u'资产管理员表'
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name

# 合同信息
class Contracts(models.Model):
    sn = models.CharField(max_length=64, verbose_name=u'合同编号')
    title = models.CharField(max_length=25, null=True, verbose_name=u'合同标题')
    cost = models.IntegerField(null=True, blank=True, verbose_name=u'合同金额')
    start_date = models.DateTimeField(verbose_name=u'起始时间')
    end_date = models.DateTimeField(verbose_name=u'到期时间')
    abstract = models.TextField(null=True, blank=True, verbose_name=u'合同摘要')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    file_name = models.CharField(max_length=64, null=True, blank=True, verbose_name=u'合同文件')
    file_path = models.CharField(max_length=128, null=True, blank=True, verbose_name=u'合同路径')

    class Meta:
        verbose_name = u'合同表'
        verbose_name_plural= u'合同表'
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
  
# IDC机房信息
class IDC(models.Model):
    name = models.CharField(max_length=25, verbose_name=u'机房名')
    region = models.CharField(max_length=25, verbose_name=u'地区')
    provider = models.CharField(max_length=25, null=True, verbose_name=u'运营商')
    contacts = models.ForeignKey(Manager, null=True, blank=True, verbose_name=u'负责人')
    address = models.CharField(max_length=128, null=True, verbose_name=u'机房地址')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    contract = models.ForeignKey(Contracts, null=True, blank=True, verbose_name=u'合同')

    class Meta:
        verbose_name = u'IDC机房表'
        verbose_name_plural= u'IDC机房表'
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name

# 机柜信息
class Cabinets(models.Model):
    number = models.CharField(max_length=25, verbose_name=u'机柜编号')

    class Meta:
        verbose_name = u'机柜表'
        verbose_name_plural= u'机柜表'
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name

# IP资源池信息
class IPAddrPool(models.Model):
    idc = models.ForeignKey(IDC, null=True, blank=True, verbose_name=u'所属机房')
    segment = models.GenericIPAddressField(verbose_name=u'IP网段')
    netmask = models.GenericIPAddressField(verbose_name=u'子网掩码')

    class Meta:
        verbose_name = u'IP资源池表'
        verbose_name_plural= u'IP资源池表'
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name

# 主机组信息
class AssetGroup(models.Model):
    name = models.CharField(max_length=25, verbose_name=u'组名')

    class Meta:
        verbose_name = u'主机组表'
        verbose_name_plural= u'主机组表'
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name

# 设备类型信息
class DeviceType(models.Model):
    name = models.CharField(max_length=25)
    memo = models.TextField(null=True, blank=True, verbose_name=u'备注')

    class Meta:
        verbose_name = u'设备类型表'
        verbose_name_plural= u'设备类型表'
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name

# 主机列表信息
class Assets(models.Model):
    hostname = models.CharField(max_length=64, unique=True, blank=True, verbose_name=u'主机名')
    device_type = models.ForeignKey(DeviceType, verbose_name=u'设备类型')
    cabinet_num = models.ForeignKey(Cabinets, verbose_name=u'机柜编号')
    cabinet_order = models.CharField(max_length=25, null=True, blank=True, verbose_name=u'机柜序号')
    memo = models.TextField(null=True, blank=True, verbose_name=u'备注')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=u'创建日期')
    update_at = models.DateTimeField(auto_now=True, verbose_name=u'更新日期')
    idc = models.ForeignKey(IDC, verbose_name=u'机房')
    contract = models.ForeignKey(Contracts, null=True, blank=True, verbose_name=u'合同')
    
    class Meta:
        verbose_name = u'主机表'
        verbose_name_plural= u'主机表'
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name  
    
    