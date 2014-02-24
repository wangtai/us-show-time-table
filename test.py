import urllib

__author__ = 'wangtai'

import unittest

url = 'http://www.yyets.com/tv/schedule'

class MyTestCase(unittest.TestCase):
    def test_something(self):
        html_text =  urllib.urlopen(url).read()
        html_text_utf8 = html_text
        from time_table_data_source import Yyets
        parser = Yyets()
        parser.feed(html_text_utf8)
        print parser.time_table
        self.assertNotEqual(parser.time_table, '')


if __name__ == '__main__':
    unittest.main()
