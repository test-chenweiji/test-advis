# coding=utf-8

database = {
    'cookies': '',
    'placeholders': [],
    'placeholders_detail': {},
    'macros': {},
    # 保存将要用到的cpl, key: cpl_uuid, value: cpl的相关数据
    'cpls': {},
    # 保存新增的占位符数据 key: 占位符名称 value: {uuid/name}
    'new_placeholders': {},
    # 要初始化的内容包设置
    'new_content_packs_setting': {},
    # 重新获取得到的内容包 key: 内容包命名 value: {uuid/name .etc}
    'regain_content_packs': {},
    # 快捷指令数组
    'shortcut_instructions': [],
    # 用于保存设备组信息 key: 设备组名, value: [{group_name: {device: [], automations[]} device / .etc}]
    'device_groups': {},
    # 用于保存当前忽略驱动列表
    'ignored_drives': [],

    # 保存需要初始化播放列表数据
    'playlist_init': [],
    # 初始化播放列表需要用到的数据
    'playlist': []

}