# coding=utf-8
import root
import os
import time
import logging
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
from project.operation.impl.send_pack_screenvision1 import pack_screenvision
from project.operation.impl.send_pack_screenvision2 import pack_screenvision2
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
        #配置->通用->Advanced->pos_spl_mapping_enabled 开关
        InitAdvancedSpl(server_url).execute()
        #配置->通用->POS设置
        InitPOSSetting(server_url).execute()
        #配置->影院设备
        InitPOSSystem(server_url).execute()
        #查询POS信息
        query_pos()
        #下发pack(screevision样本、ncm样本)
        pack_screenvision()
        #创建、查询占位符
        Create_Placeholder(server_url).execute()
        GetPlaceholderUuid(server_url).execute()
        #创建playlist
        CreatePlaylist(server_url).execute()
        #playlist匹配POS场次
        PosMapping(server_url).execute()

        #获取POS
        f = open(root.get_root_path() + "/output/pos_info.txt", "r")
        datalist = f.readlines()[1:2]
        screen = datalist[0][:36]
        screen1 = screen.replace('\n', '')

        f1 = open(root.get_root_path() + "/output/pos_info.txt", "r")
        datalist2 = f1.readlines()[2:3]
        start = datalist2[0][:36]
        start1 = start.replace('\n', '')

        f2 = open(root.get_root_path() + "/output/pos_info.txt", "r")
        datalist3 = f2.readlines()[4:5]
        feature_title = datalist3[0][:36]
        feature_title1 = feature_title.replace('\n', '')

        #统计测试结果变量
        send_pack = True
        delete_pack = True
        alter_pack = True
        alter_delete= True

        #排期同步
        ScheduleSync(server_url).execute()
        print ("下发Pack且排期同步后，期望结果：\n"+ screen1 + "号厅" + feature_title1 +'影片在'+ start1 + "场次应添加对应占位符匹配的内容包CPL")
        logging.info("下发Pack且排期同步后，期望结果：\n %s号厅 %s影片在 %s场次应添加对应占位符匹配的内容包CPL" % (screen1,feature_title1,start1))
        time.sleep(30)
        print ("排期同步完成校验排期，实际结果：")
        logging.info("排期同步完成校验排期，实际结果：")
        res = performance()
        print(res)
        logging.info(res)
        if '已添加' in res:
            print('测试结果：通过\n')
            logging.info('测试结果：通过\n')
        else:
            print('测试结果：不通过！！！\n')
            send_pack = False
            logging.info('测试结果：不通过！！！\n')


        time.sleep(20)
        #查询pack、删除pack
        #query_pack()
        #delete_pack()
        delete_pack2()
        # 排期同步
        ScheduleSync(server_url).execute()
        print ("删除Pack且排期同步后，期望结果：\n" + screen1 + "号厅" + feature_title1 + '影片在' + start1 + "场次找不到对应占位符匹配的内容包（保护场次不受Pack删除影响）")
        logging.info("删除Pack且排期同步后，期望结果：\n %s号厅 %s影片在 %s场次找不到对应占位符匹配的内容包（保护场次不受Pack删除影响）" % (screen1,feature_title1,start1))
        #time.sleep(30)
        print ("排期同步完成校验排期，实际结果：")
        logging.info ("排期同步完成校验排期，实际结果：")
        res = performance()
        print(res)
        logging.info(res)
        if '未找到' in res:
            print('测试结果：通过\n')
            logging.info('测试结果：通过\n')
        elif '保护场次' in res:
            print('测试结果：通过\n')
            logging.info('测试结果：通过\n')
        else:
            print('测试结果：不通过！！！\n')
            delete_pack = False
            logging.info('测试结果：不通过！！！\n')
        time.sleep(20)

        #下发pack(screevision样本、ncm样本)
        pack_screenvision2()
        # 排期同步
        ScheduleSync(server_url).execute()
        print ("修改Pack且排期同步后，期望结果：\n" + screen1 + "号厅" + feature_title1 + '影片在' + start1 + "场次应添加对应占位符匹配的内容包CPL（保护场次不受Pack修改影响）")
        logging.info("修改Pack且排期同步后，期望结果：\n %s号厅 %s影片在 %s场次应添加对应占位符匹配的内容包CPL（保护场次不受Pack修改影响）" % (screen1,feature_title1,start1))
        time.sleep(30)
        print ("排期同步完成校验排期，实际结果：")
        logging.info ("排期同步完成校验排期，实际结果：")
        res = performance()
        print(res)
        logging.info(res)
        if '已添加' in res:
            print('测试结果：通过\n')
            logging.info('测试结果：通过\n')
        else:
            print('测试结果：不通过！！！\n')
            alter_pack = False
            logging.info('测试结果：不通过！！！\n')

        time.sleep(20)
        # 查询pack、删除pack
        # query_pack()
        # delete_pack()
        delete_pack2()
        # 排期同步
        ScheduleSync(server_url).execute()
        print ("删除Pack且排期同步后，期望结果：\n" + screen1 + "号厅" + feature_title1 + '影片在' + start1 + "场次找不到对应占位符匹配的内容包（保护场次不受Pack删除影响）")
        logging.info ("删除Pack且排期同步后，期望结果：\n" + screen1 + "号厅" + feature_title1 + '影片在' + start1 + "场次找不到对应占位符匹配的内容包（保护场次不受Pack删除影响）")
        time.sleep(30)
        print ("排期同步完成校验排期，实际结果：")
        logging.info("排期同步完成校验排期，实际结果：")
        res = performance()
        print(res)
        logging.info(res)
        if '未找到' in res:
            print('测试结果：通过\n')
            logging.info('测试结果：通过\n')
        elif '保护场次' in res:
            print('测试结果：通过\n')
            logging.info('测试结果：通过\n')
        else:
            print('测试结果：不通过！！！\n')
            alter_delete = False
            logging.info('测试结果：不通过！！！\n')

        print('Advis测试结果统计：')
        logging.info('Advis测试结果统计：')
        if send_pack:
            print('Pack下发测试结果: %s' %  '通过' )
            logging.info('Pack下发测试结果: %s' % '通过')
        else:
            print('Pack下发测试结果: %s' % '不通过')
            logging.info(('Pack下发测试结果: %s' % '不通过'))

        if delete_pack:
            print('Pack删除测试结果: %s' %  '通过' )
            logging.info('Pack删除测试结果: %s' % '通过')
        else:
            print('Pack删除结果: %s' % '不通过')
            logging.info(('Pack删除测试结果: %s' % '不通过'))

        if alter_pack:
            print('Pack修改测试结果: %s' %  '通过' )
            logging.info('Pack修改测试结果: %s' % '通过')
        else:
            print('Pack修改测试结果: %s' % '不通过')
            logging.info(('Pack修改测试结果: %s' % '不通过'))

        if alter_delete:
            print('Pack删除测试结果: %s' %  '通过' )
            logging.info('Pack删除测试结果: %s' % '通过')
        else:
            print('Pack删除测试结果: %s' % '不通过')
            logging.info(('Pack删除测试结果: %s' % '不通过'))

        print('\n')

        # logging.info(('Pack下发测试结果: %s' %  '通过' if send_pack else '不通过！！！'))
        # print('Pack删除测试结果: %s' % '通过' if delete_pack else '不通过！！！')


if __name__ == '__main__':
    init = InitRunner()
