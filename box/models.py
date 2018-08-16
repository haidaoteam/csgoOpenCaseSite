from __future__ import unicode_literals

from django.db import models
from django.utils import timezone as dt
from django.utils.translation import ugettext as _l, ugettext_lazy as _
from uuid import uuid1, UUID

from social_auth.models import SteamUser


class ModelBase(models.Model):
    uid = models.CharField(unique=True, editable=False, max_length=63, verbose_name=_("UID"))
    create_time = models.DateTimeField(editable=False, auto_now_add=True, verbose_name=_("Create Time"))
    update_time = models.DateTimeField(editable=False, auto_now=True, verbose_name=_("Update Time"))

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = uuid1().hex
        super(ModelBase, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class AssetItem(ModelBase):
    appid = models.CharField(max_length=8)
    contextid = models.CharField(max_length=8)
    classid = models.CharField(max_length=32)
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    icon_url = models.CharField(max_length=512, default=None, null=True, blank=True)
    icon_url_large = models.CharField(max_length=512, default=None, null=True, blank=True)
    exterior = models.CharField(max_length=64, default=None, null=True, blank=True)
    rarity = models.CharField(max_length=64, default=None, null=True, blank=True)
    rarity_color = models.CharField(max_length=32, default=None, null=True, blank=True)
    type = models.CharField(max_length=64, default=None, null=True, blank=True)
    quality = models.CharField(max_length=64, default=None, null=True, blank=True)
    quality_color = models.CharField(max_length=32, default=None, null=True, blank=True)
    weapon = models.CharField(max_length=64, default=None, null=True, blank=True)
    s_name = models.CharField(max_length=128, default=None, null=True, blank=True, verbose_name=_('Name'))
    s_type = models.CharField(max_length=128, default=None, null=True, blank=True, verbose_name=_('Type'))
    price = models.FloatField(default=0.0)

    class Meta:
        verbose_name = _('Asset Item')
        verbose_name_plural = _('Asset Item')

    def __str__(self):
        return self.name


class Case(ModelBase):
    name = models.CharField(max_length=128, verbose_name=_("Name"))
    key = models.CharField(max_length=128, unique=True, verbose_name=_('Key'))
    price = models.FloatField(default=0, verbose_name=_('Price'))
    cover_weapon = models.ImageField(upload_to='cases', default=None, blank=True, null=True, verbose_name=_('Weapon Image'))
    cover_case = models.ImageField(upload_to='cases', default=None, blank=True, null=True, verbose_name=_('Case Image'))
    enable = models.BooleanField(default=True, verbose_name=_('Enable'))

    class Meta:
        verbose_name = _('Case')
        verbose_name_plural = _('Case')

    def __str__(self):
        return self.name
