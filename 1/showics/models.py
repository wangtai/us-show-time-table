#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (i@wangtai.me)

"""docstring
"""

__revision__ = '0.1'

from django.db import models


class ShowTableIcs(models.Model):
    # uid
    uid = models.CharField(max_length=255, unique=True, primary_key=True)
    # title
    title = models.CharField(max_length=255, null=False)
    # description
    description = models.CharField(max_length=255)
    # date
    date = models.DateField()
    class Meta(object):
        db_table = 'show_table_ics'