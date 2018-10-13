# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 08:33:16 2018

@author: chen
"""

from django.contrib import admin
from django.urls import path ,re_path, include
from myapp import views as myapp_views

app_name = 'myapp'

urlpatterns = [
    path('index/', myapp_views.index, name='index'),
    re_path(r'market/(\d+)', myapp_views.market, name='market'),
    path('cart/', myapp_views.cart, name='cart'),
    path('my/', myapp_views.my, name='my'),
]
