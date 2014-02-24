#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (i@wangtai.me)

"""
获得yyets数据
"""

__revision__ = '0.1'

from HTMLParser import HTMLParser


class Yyets(HTMLParser):
    """
    http:http://www.yyets.com/tv/schedule
    """

    time_table = {}
    def __init__(self):
        self.inTimeTable = False
        self.inDt = False
        self.inSpan = False

        self.date = ''
        self.dataSeqId = -1
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'table' and ('class', 'playTime_tv') in attrs:
            self.inTimeTable = True
        if tag == 'dt':
            self.inDt = True
        if tag == 'dd':
            self.inDD = True
            self.dataSeqId += 1
        if self.inTimeTable and self.inDD and tag == 'a':
            for n, v in attrs:
                if 'href' == n:
                    if self.dataSeqId not in self.time_table[self.date]:
                        self.time_table[self.date].setdefault(self.dataSeqId, {})
                    self.time_table[self.date][self.dataSeqId].setdefault('url', v)
                    break;
        if tag == 'span':
            self.inSpan = True
        pass


    def handle_data(self, data):
        if self.inTimeTable and self.inDt:
            self.date = data
            if data not in self.time_table:
                self.time_table.setdefault(data,{})
        if self.inTimeTable and self.inDD and self.inSpan:
            self.time_table[self.date][self.dataSeqId].setdefault('title', data)
        pass


    def handle_endtag(self, tag):
        if tag == 'dt':
            self.inDt = False
        if tag == 'table' and self.inTimeTable:
            self.inTimeTable = False
        if tag == 'dd':
            self.inDD = False
        if tag == 'span':
            self.inSpan = False
        pass