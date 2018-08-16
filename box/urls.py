#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from box import views

urlpatterns = [
    url(r'^$', views.home_page, name='index_page'),
    url(r'^api/', include('box.api.urls'))
]
