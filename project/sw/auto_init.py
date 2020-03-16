# coding=utf-8
import root
import os
import time
from project.database import sw_db
from device_init.init_device_batch_multi import InitDeviceBatchMulti
from project.operation.impl.init_advanced_spl import InitAdvancedSpl
from project.operation.impl.init_pos_setting import InitPOSSetting
from project.operation.impl.init_pos_system import InitPOSSystem
from project.operation.impl.login import Login
from project.utils.config_reader import ConfigReader
from project.operation.impl.init_auto_spl_mapping import InitAutoSplMapping
from project.operation.impl.create_playlist_uuid import CreatePlaylistUuid
from project.operation.impl.creat_playlist import CreatePlaylist
from project.operation.impl.get_lms_uuid import GetLmsUuid
from project.operation.impl.create_placeholder import Create_Placeholder
from project.operation.impl.get_placeholder_uuid import GetPlaceholderUuid
from project.operation.impl.pos_mapping import PosMapping
from project.operation.impl.schedule_sync import ScheduleSync
from project.operation.impl.performance_datetime import performance
from project.operation.impl.get_pos_info import query_pos
#from project.operation.impl.send_pack_screenvision1 import pack_screenvision
from project.operation.impl.send_pack_ncm1 import pack_ncm
from project.operation.impl.send_pack_ncm2 import pack_ncm2
# from project.operation.impl.query_pack import query_pack
# from project.operation.impl.delete_pack import delete_pack
from project.operation.impl.delete_pack2 import delete_pack2

class InitRunner(object):

    def __init__(self):
        pass

    def multi_run(self, cvs_path):
        # 初始化多服务器设备
        InitDeviceBatchMulti(root.get_root_path() + cvs_path).execute()

    def single_run(self):
        ConfigReader.read_config()
        server_url = ConfigReader.get_string('server', 'url')
        username = ConfigReader.get_string('account', 'username')
        password = ConfigReader.get_string('account', 'password')

        # 模拟登陆
        Login(server_url, username, password).execute()
        #生成LMS的uuid到一个txt文件上
        GetLmsUuid(server_url).execute()
        # 配置->通用->Advanced->pos_spl_mapping_enabled 开关
        # InitAdvancedSpl(server_url).execute()
        # 配置->通用->POS设置
        InitPOSSetting(server_url).execute()
        # 配置->影院设备
        InitPOSSystem(server_url).execute()
        #查询POS信息
        query_pos()
        # 下发pack(screevision样本、ncm样本)
        #pack_screenvision()
        pack_ncm()
        #创建、查询占位符
        Create_Placeholder(server_url).execute()
        GetPlaceholderUuid(server_url).execute()
        #创建playlist
        CreatePlaylist(server_url).execute()
        #playlist匹配POS场次
        PosMapping(server_url).execute()
        #排期同步
        ScheduleSync(server_url).execute()
        time.sleep(30)
        print ("下发pack且排期同步后，校验排期：")
        performance()

        time.sleep(30)
        #查询pack、删除pack
        # query_pack()
        # delete_pack()
        delete_pack2()
        # 排期同步
        ScheduleSync(server_url).execute()
        time.sleep(30)
        print ("删除pack且排期同步后，校验排期：")
        performance()
        time.sleep(30)

        # 下发pack(screevision样本、ncm样本)
        #pack_screenvision()
        pack_ncm2()
        # 排期同步
        ScheduleSync(server_url).execute()
        time.sleep(30)
        print ("修改pack且排期同步后，校验排期：")
        performance()

        time.sleep(30)
        # 查询pack、删除pack
        # query_pack()
        # delete_pack()
        delete_pack2()
        # 排期同步
        ScheduleSync(server_url).execute()
        time.sleep(30)
        print ("删除pack且排期同步后，校验排期：")
        performance()

if __name__ == '__main__':
    init = InitRunner()
