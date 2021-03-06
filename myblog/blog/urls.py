#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/12/4
# @Desc  :

from django.contrib import admin
from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path(r'',views.index,name = 'index'),
    # path(r'index/', views.index,name = 'index'),
    path('blog/', views.blog,name = 'blogspage'),
    path('article/<slug:article_id>/', views.article_page ,name='article_page'),
    path('edit/<slug:article_id>/', views.edit_page ,name='edit_page'),
    path('edit_action/', views.edit_action ,name='edit_action'),
    path('delete/<slug:article_id>/', views.delete_article ,name='delete_article'),
    path('suggest', views.SearchSuggest.as_view(), name='suggest'),
    path('searchview', views.SearchView.as_view(),name="searchview"),
]
