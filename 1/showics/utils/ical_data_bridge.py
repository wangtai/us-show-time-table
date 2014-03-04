#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (i@wangtai.me)

"""
把网上的数据处理成ical格式
BEGIN:VCALENDAR
VERSION:2.0
X-APPLE-LANGUAGE:zh
X-APPLE-REGION:CN
X-WR-CALNAME:中国节假日
PRODID:-//hacksw/handcal//NONSGML v1.0//EN
BEGIN:VEVENT
UID:uid1@example.com
DTSTAMP:19970714T170000Z
ORGANIZER;CN=John Doe:MAILTO:john.doe@example.com
DTSTART:19970714T170000Z
DTEND:19970715T035959Z
SUMMARY:Bastille Day Party
UID:fea40780-6f35-341b-a3a4-a3951cce6c12
END:VEVENT
END:VCALENDAR
"""

__revision__ = '0.1'

import uuid

def ical_data(year, month, time_table, special_ids = []):
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
    :param special_ids: []
    :rtype : str
    """

    data = 'BEGIN:VCALENDAR\n'
    data += 'VERSION:2.0\n'
    data += 'PRODID:-//wangtai//US_SHOW_TABLE//CN\n'
    data += 'X-APPLE-LANGUAGE:zh\n'
    data += 'X-APPLE-REGION:CN\n'
    data += 'X-WR-CALNAME:美剧时间表\n'

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
            show_id = event['url'].split('/')[-1]
            if show_id not in special_ids and len(special_ids) != 0:
                continue
            data += 'BEGIN:VEVENT\n'
            data += 'DTSTART;VALUE=DATE:{0}\n'.format(s_date)
            data += 'DTEND;VALUE=DATE:{0}\n'.format(s_date)
            data += 'SUMMARY:{0} ({1})\n'.format(event['title'], event['url'])
            # s_uuid = str(uuid.uuid1())
            s_uuid = '{}_{}_{}_{}'.format(year, s_month, s_date, show_id)
            data += 'UID:{0}\n'.format(s_uuid)
            data += 'END:VEVENT\n'
    data += 'END:VCALENDAR'

    return data
