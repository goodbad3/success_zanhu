#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from django.urls import path

from zanhu.users import views

app_name = "users"
urlpatterns = [
    path("update/", views.UserUpdateView.as_view(), name="update"),
    path("<str:username>/", views.UserDetailView.as_view(), name="detail"),
]
#http://127.0.0.1:8005/users/root/ -->> detail
#http://127.0.0.1:8005/users/update/ -->>update