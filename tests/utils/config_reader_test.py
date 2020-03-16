# coding=utf-8
import unittest

from project.utils.config_reader import ConfigReader


class TestConfigReader(unittest.TestCase):

    def test_read_config(self):
        cf = ConfigReader.read_config()
        self.assertIsNotNone(cf)

    def test(self):
        df = {"name": "Lon"}
        print(df["name"])
        # print(df["age"])

if __name__ == '__main__':
    unittest.main()
