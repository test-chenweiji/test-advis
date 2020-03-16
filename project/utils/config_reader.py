# coding=utf-8
import configparser
import json
import os
import root


class ConfigReader(configparser.ConfigParser):

    CONFIG = {}

    def optionxform(self, optionstr):
        return optionstr

    @staticmethod
    def read_config():
        root_dir = root.get_root_path()
        cf = ConfigReader()
        # cf = configparser.ConfigParser()
        cf.read(root_dir + "/config.ini", encoding="utf-8-sig")
        # secs = cf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])，并以列表的形式返回
        # print(secs)
        ConfigReader.CONFIG = cf
        return cf

    @staticmethod
    def get_string(section, key):
        return ConfigReader.CONFIG.get(section, key)

    @staticmethod
    def get_array(section, key):
        conf_str = ConfigReader.CONFIG.get(section, key)
        return conf_str.split(",")

    @staticmethod
    def get_options_array(section, no_repeat=False):
        arr = ConfigReader.CONFIG.options(section)
        if no_repeat:
            arr = list(set(arr))
        return arr

    @staticmethod
    def get_json_map(section):
        options = ConfigReader.CONFIG.items(section)
        res = {}
        for item in options:
            res[item[0]] = json.loads(item[1])
        return res

    # 获取json数组
    @staticmethod
    def get_json_array(section):
        options = ConfigReader.CONFIG.items(section)
        res = []
        for item in options:
            data = json.loads(item[1])
            # data['iniKey'] = item[0]
            res.append(data)
        return res

    @staticmethod
    def set_value(section, option, value):
        ConfigReader.CONFIG.set(section, option, value)

    @staticmethod
    def write_value(file):
        ConfigReader.CONFIG.write(open(file, "r+", encoding="utf-8-sig"))


if __name__ == '__main__':
    ConfigReader.read_config()
