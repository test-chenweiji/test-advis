# coding=utf-8

class LoginException(Exception):
    def __init__(self, error_info):
        super().__init__(self)
        self.error_info = error_info

    def __str__(self):
        return self.error_info


if __name__ == '__main__':
    try:
        raise LoginException('DBQuery数据查询异常')
    except LoginException as e:
        print(e)
