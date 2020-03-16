# coding=utf-8

global_values = {
    'index': 0
}

device_defaults = {
    'sms':{
        'christie':{
            'port':'4502',
            'api_username': 'service',
            'api_password': 'service',
            'ftp_port': '21',
            'ftp_username': 'ftpuser',
            'ftp_password': 'ftptms'
        },
        'christie_series_3':{
            'port':'5001',
            'api_username': 'service',
            'api_password': 'service',
            'ftp_port': '21',
            'ftp_username': 'ftpuser',
            'ftp_password': 'ftptms'
        },
        'dolby':{
            'port':'8080',
            'ftp_port':'21',
            'ftp_username':'dolbyftp',
            'ftp_password':'dolbyftp'
        },
        'doremi':{
            'port':'11730',
            'ftp_port':'21',
            'ftp_username':'manager',
            'ftp_password':'password'
        },
        'imax':{
            'port':'11738'
        },
        'sony':{
            'port':'443',
            'api_username': 'super',
            'api_password': '0955',
            'ftp_port':'21',
            'ftp_username':'s2suser',
            'ftp_password':'sahbicwd'
        },
        'qube':{
            'port':'8080',
            'ftp_port':'21',
            'ftp_username': 'anonymous',
            'ftp_password': 'anonymous'
        },
        'gdc':{
            'port':'49153',
            'ftp_port':'21',
            'ftp_username':'content',
            'ftp_password':'content'
        },
        'emulator':{
            'ip':'127.0.0.1',
            'port': '9001'
        },
        'barco': {
            'port':'43758',
            'ftp_port':'21',
            'api_username': 'admin',
            'api_password': 'Admin1234',
            'ftp_username':'ftpdcps',
            'ftp_password':'icmp'
        },
        'usl': {
            'port': '43759',
            'ftp_port': '21',
            'api_username': 'installer',
            'api_password': 'installer'
        }
    },
    'projector':{
        'christie':{
            'port':'5000'
        },
        'nec':{
            'port':'7142'
        },
        'barco':{
            'port':'5000'
        },
        'emulator':{
            'ip':'127.0.0.1',
            'port': '9001'
        },
        'sony':{
            'port':'443',
            'api_username': 'super',
            'api_password': '0955'
        },
        'imax':{
            'port':'11738'
        }
    },
    'camera':{
        'axis':{
            'port':'80',
            'api_username':'root',
            'api_password':'root'
        },
        'foscam':{
            'port':'80',
            'api_username':'aam',
            'api_password':'aam'
        }
    },
    'audio':{
        'dolby':{
        },
        'usl':{
            'port': '10001'
        },
        'qsc':{
            'port': '4446'
        }
    },
    'pos':{
        'emulator':{
            'ip': '127.0.0.1',
            'port': '8999'
        }
    }
}