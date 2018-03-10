# -*- coding: utf-8 -*-
__author__ = 'wangruiyy'
__date__ = '2018/3/8 下午4:59'

from django.conf.urls import url, include
from .views import OrgView, AddUserAskView

urlpatterns = [
    # 机构课程列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask')



        ]