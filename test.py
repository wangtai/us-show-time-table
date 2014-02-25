import urllib

__author__ = 'wangtai'

import unittest

url = 'http://www.yyets.com/tv/schedule'


class MyTestCase(unittest.TestCase):



    def test_time_table(self):
        html_text =  urllib.urlopen(url).read()
        html_text_utf8 = html_text
        from time_table_data_source import Yyets
        parser = Yyets()
        parser.feed(html_text_utf8)
        # print parser.time_table
        time_table = parser.time_table
        from ical_data_bridge import ical_data
        print ical_data(2014,2, time_table)
        self.assertNotEqual(parser.time_table, '')

    def test_ical_data_bridge(self):
        from ical_data_bridge import ical_data
        # print ical_data(2014,2, {})
        pass


if __name__ == '__main__':
    unittest.main()
