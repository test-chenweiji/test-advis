# coding=utf-8
import requests

from project.database import sw_db
from project.operation.base.request_operation import RequestOperation

class ScheduleSync(RequestOperation):

    # def __init__(self, url):
    #     super().__init__(url)

    def request(self):
        data = {
	"eval_string": " self.task_manager.run_named_task(\"Schedules Synchroniser\")"
}
        resp = requests.post(self._url + '/core/introspect',
                             json=data,
                             cookies=sw_db.database['cookies'])
        return resp
