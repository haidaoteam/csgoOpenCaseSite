#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "casedemo.settings")
channel_layer = channels.asgi.get_channel_layer()

