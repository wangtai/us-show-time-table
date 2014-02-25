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

def ical_data(year, month, time_table):
    """

    :param year: int
    :param month: int
    :param time_table:
                    http://www.yyets.com/tv/schedule
                    {'1号': {
                        seqid: {
                            'url': 'xxx',
                            'title': 'yyy'
                        }
                    }}
    :rtype : str
    """

    data = 'BEGIN:VCALENDAR\n'
    data += 'VERSION:2.0\n'
    data += 'PRODID:-//wangtai//US_SHOW_TABLE//CN\n'
    for s_date, event_list in time_table.iteritems():
        # print "%s %s" % (s_date, event_list)
        date = int(s_date[:-3])
        if date < 10:
            s_date = '0%s' % date
        else:
            s_date = str(date)
        if month < 10:
            s_month = '0%s' % month
        else:
            s_month = str(month)
        s_date = "%s%s%s" % (year, s_month, s_date)
        for seqid, event in event_list.iteritems():
            data += 'BEGIN:VEVENT\n'
            data += 'DTSTART;VALUE=DATE:%s\n' % s_date
            data += 'DTEND;VALUE=DATE:%s\n' % s_date
            data += 'SUMMARY:%s (%s)\n' % (event['title'], event['url'])
            data += 'END:VEVENT\n'
    data += 'END:VCALENDAR'

    return data