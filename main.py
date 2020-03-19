# coding=utf-8
from project.sw.auto_init import InitRunner
#from project.sw.auto_init2 import InitRunner
import time
import os
import logging
def main():
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.INFO,
                        filename='pack.log',
                        filemode='a')
    logging.info('Screenwriter初始化设备')
    print ('Screenwriter初始化设备')
    InitRunner().multi_run('/device_cvs/Automation.csv')
    print("Advis自动化操作:\n")
    logging.info("Advis自动化操作:\n")
    #下发pack、删除pack校验排期
    InitRunner().single_run()
    print('日志已输出到pack.log文件')
    input('输入任意键退出...')
    #删除pack校验排期
    #InitRunner2().single_run2()
    # InitRunner().multi_run('/device_cvs/Automation.csv')
    # while True:
    #     print('输入您需要的操作:')
    #     print('1: screenwriter初始化设备')
    #     print('2: 下发pack、删除pack校验排期')
    #     print('3: 退出')
    #     operation = input('操作:').strip()
    #     if operation == '1':
    #         InitRunner().multi_run('/device_cvs/Automation.csv')
    #     elif operation == '2':
    #         InitRunner().single_run()
    #     elif operation == '3':
    #         break
    #     else:
    #         print('warning: 未知操作')





if __name__ == '__main__':
    main()
