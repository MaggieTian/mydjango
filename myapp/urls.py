#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/30
# @Author  : tianqi
# @File    : urls.py

from  django.conf.urls import  url

from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    #url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]