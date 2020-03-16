## 所需环境
文件为可执行文件，无需环境

## 代码拉取
- git clone git@gitlab.aamcn.com.cn:aam/verifier.git
- git checkout sw_auto_init_new

## 运行
- 运行前请确保服务器上已上传了对应的黑场文件与视频文件
- 如果需要导入device_cvs，请将导入的文件名改为Automation.csv
###windows系统:
- 进入项目根目录
- 执行根目录的main.exe文件
###linux系统:
- 进入项目根目录
- 在根目录执行 ./main

## 修改功能概括
- 初始化同步设置
- 初始化广告占位符
- 初始化服务器设备

## 配置相关
#### 配置文件在根目录下的config.ini
1.account: 登录用户账号与密码, 注意必须登录最高权限的用户, 否则部分自动化指令无法执行

2.server: 目标服务器域名

