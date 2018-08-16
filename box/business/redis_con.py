#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
from django.conf import settings

pool = None


def init_conn():
    global pool
    pool = redis.ConnectionPool(host=settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD, db=settings.REDIS_DB_INDEX)


def get_redis():
    global pool
    r = redis.Redis(connection_pool=pool)
    return r

