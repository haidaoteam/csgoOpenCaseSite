#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import random
from uuid import uuid1

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


def ref_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def uid_generator():
    return uuid1().hex


class SteamUserManager(BaseUserManager):
    def _create_user(self, steamid, password, **extra_fields):
        """
        Creates and saves a User with the given steamid and password.
        """
        try:
            # python social auth provides an empty email param, which cannot be used here
            del extra_fields['email']
        except KeyError:
            pass
        if not steamid:
            raise ValueError('The given steamid must be set')
        user = self.model(steamid=steamid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, steamid, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(steamid, password, **extra_fields)

    def create_superuser(self, steamid, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(steamid, password, **extra_fields)


class SteamUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'steamid'

    steamid = models.CharField(max_length=17, unique=True)
    uid = models.CharField(max_length=128, unique=True, default=uid_generator)
    personaname = models.CharField(max_length=255)
    profileurl = models.CharField(max_length=300)
    avatar = models.CharField(max_length=255)
    avatarmedium = models.CharField(max_length=255)
    avatarfull = models.CharField(max_length=255)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.personaname

    def get_short_name(self):
        return self.personaname

    def get_full_name(self):
        return self.personaname

    class Meta:
        verbose_name = _('Steam User')
        verbose_name_plural = _('Steam Users')
