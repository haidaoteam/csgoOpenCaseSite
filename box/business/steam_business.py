import json
import time
import logging
import requests
import threading
import random

from django.conf import settings
from django.db import connection
from django.utils import timezone as dt
from django.utils.translation import ugettext_lazy as _

_inventory_url_base = 'http://steamcommunity.com/inventory/{steamid}/{appid}/{contextid}?l=english&count=2000&start_assetid={s_assetid}'

_logger = logging.getLogger(__name__)


AssetKeysMap = {
    'name': 'name',
    'market_name': 'market_name',
    'market_hash_name': 'market_hash_name',
    'icon_url': 'icon_url',
    'icon_url_large': 'icon_url_large',
    'tags': 'tags'
}


def is_connection_usable():
    try:
        if connection.connection is not None:
            connection.connection.ping()
    except Exception as e:
        _logger.error(e)
        return False
    else:
        return True


def get_user_inventory(steamid, s_assetid=None, **kwargs):
    try:
        t_url = _inventory_url_base.format(
            steamid=steamid, appid='730', contextid='2', s_assetid=s_assetid)
        resp = requests.get(t_url, timeout=10000)
        body = json.loads(resp.content, encoding='utf-8')
        return body
    except Exception as e:
        _logger.exception(e)
    return None
