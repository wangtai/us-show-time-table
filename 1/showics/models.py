#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (i@wangtai.me)

"""docstring
"""

__revision__ = '0.1'

from django.db import models


class ShowTableIcs(models.Model):
    uid = models.CharField(max_length=255, unique=True, primary_key=True)
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255)
    date = models.DateField()

    class Meta(object):
        db_table = 'show_table_ics'


class ShowList(models.Model):
    show_id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255, unique=True, null=False)

    class Meta(object):
        db_table = 'show_list'