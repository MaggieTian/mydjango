#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/30
# @Author  : tianqi
# @File    : urls.py

from  django.conf.urls import  url

from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
]