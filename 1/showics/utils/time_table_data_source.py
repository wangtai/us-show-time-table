#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (i@wangtai.me)

"""
获得yyets数据
"""
import urllib

__revision__ = '0.1'

from HTMLParser import HTMLParser
from ical_data_bridge import ical_data


def read_time_table(year, month):
    """
    :rtype : {}
    :param year: int
    :param month: int
    """
    if month < 10:
        s_month = '0%s' % month
    else:
        s_month = str(month)
    url = 'http://www.yyets.com/tv/schedule/index/year/{0}/month/{1}'.format(year, s_month)
    html_text = urllib.urlopen(url).read()
    parser = Yyets()
    parser.feed(html_text)
    time_table = parser.time_table
    return ical_data(year, month, time_table)


class Yyets(HTMLParser):
    """
    http://www.yyets.com/tv/schedule
    http://www.yyets.com/tv/schedule/index/year/2014/month/02
    {'1号': {
        seqid: {
            'url': 'xxx',
            'title': 'yyy'
        }
    }}
    """

    time_table = {}

    def __init__(self):
        HTMLParser.__init__(self)
        self.in_time_table = False
        self.in_dt = False
        self.in_font = False

        self.date = ''
        self.data_seq_id = -1

    def handle_starttag(self, tag, attrs):
        if tag == 'table' and ('class', 'playTime_tv') in attrs:
            self.in_time_table = True
        if tag == 'dt':
            self.in_dt = True
        if tag == 'dd':
            self.inDD = True
            self.data_seq_id += 1
        if self.in_time_table and self.inDD and tag == 'a':
            for n, v in attrs:
                if 'href' == n:
                    if self.data_seq_id not in self.time_table[self.date]:
                        self.time_table[self.date].setdefault(self.data_seq_id, {})
                    self.time_table[self.date][self.data_seq_id].setdefault('url', v)
                    break;
        if tag == 'font' and ('class', 'fa1') in attrs and ('style', 'color:white') not in attrs:
            self.in_font = True
        pass


    def handle_data(self, data):
        if self.in_time_table and self.in_dt:
            self.date = data
            if data not in self.time_table:
                self.time_table.setdefault(data, {})
        if self.in_time_table and self.inDD and self.in_font:
            self.time_table[self.date][self.data_seq_id].setdefault('title', data)
        pass


    def handle_endtag(self, tag):
        if tag == 'dt':
            self.in_dt = False
        if tag == 'table' and self.in_time_table:
            self.in_time_table = False
        if tag == 'dd':
            self.inDD = False
        if tag == 'font':
            self.in_font = False
        pass