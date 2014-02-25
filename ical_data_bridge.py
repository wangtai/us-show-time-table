#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (i@wangtai.me)

"""
把网上的数据处理成ical格式
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
BEGIN:VEVENT
UID:uid1@example.com
DTSTAMP:19970714T170000Z
ORGANIZER;CN=John Doe:MAILTO:john.doe@example.com
DTSTART:19970714T170000Z
DTEND:19970715T035959Z
SUMMARY:Bastille Day Party
END:VEVENT
END:VCALENDAR
"""

__revision__ = '0.1'

def ical_data(time_table):
    data = 'BEGIN:VCALENDAR'
    data += 'VERSION:2.0'
    data += 'BEGIN:VEVENT'
    data += 'DTSTART:TZID=Asia/Shanghai:19970714'
    data += 'DTEND:TZID=Asia/Shanghai:19970715'
    data += 'SUMMARY:Bastille Day Party'
    data += 'END:VEVENT'
    data += 'END:VCALENDAR'
