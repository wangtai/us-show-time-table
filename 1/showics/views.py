#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (i@wangtai.me)

"""docstring
"""

__revision__ = '0.1'

import time

from django.http import HttpResponse

from annotations import to_url
from utils import time_table_data_source
from utils import ical_data_bridge


@to_url("^$")
def index(request):
    return HttpResponse('Welcome to 美剧时间表')


@to_url('^fetch_yyets_data')
def fetch_yyets_data(request):
    i_year = int(time.strftime('%Y'))
    i_this_month = int(time.strftime('%m'))
    time_table = time_table_data_source.read_time_table(i_year, i_this_month)
    ical_data = ical_data_bridge.ical_data(i_year, i_this_month, time_table)
    return HttpResponse(ical_data)


@to_url('^time_table.ics')
def fetch_yyets_data(request):
    i_year = int(time.strftime('%Y'))
    i_this_month = int(time.strftime('%m'))
    time_table = time_table_data_source.read_time_table(i_year, i_this_month)
    ical_data = ical_data_bridge.ical_data(i_year, i_this_month, time_table)
    #Content-Type:text/calendar; charset=UTF-8
    # return HttpResponse(content=ical_data, content_type='Content-Type:text/calendar; charset=UTF-8')
    return HttpResponse(content=ical_data)