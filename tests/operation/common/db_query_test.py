# coding=utf-8
import unittest

from project.operation.common.db_query import DBQuery
from project.utils.config_reader import ConfigReader


class TestDBQuery(unittest.TestCase):

    server_url = 'http://sw02.test.aamcn.com.cn:9000'

    def test_query_one(self):
        res = DBQuery.query_one(TestDBQuery.server_url, 'playlist', "title = '2DS-EN-惊奇队长'")
        self.assertIsNotNone(res)


if __name__ == '__main__':
    unittest.main()
