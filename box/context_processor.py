#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings


def page_base_processor(request):
    context = {
        'site_title': settings.SITE_TITLE
    }
    return context
