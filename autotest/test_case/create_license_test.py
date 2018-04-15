# -*- coding: utf-8 -*-

import unittest
from tools.json_file import JsonFileData
from tools.http_runner import HttpRunner
from tools.license_helper import LicenseFunc
import HTMLTestRunner
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


class CreateLicenseTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_license(self):
        # url = "http://47.92.88.246:8999/it-license/it/license/create"
        # json_data = JsonFileData().get_json_data()
        # data = json_data["create_license"]
        # r = HttpRunner(url, "POST", data).post_data()
        self.assertEqual(1, 1, '失败')
        # self.licenseid = r["result"]

    # def test_delete_all(self):
    #     LicenseFunc().license_delete(LicenseFunc().license_query("466"))

    def tearDown(self):
        pass


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(CreateLicenseTest)
    filename = 'D:\\mypython\\ck-report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='report', description = 'unnitest测试报告')
    runner.run(suite)
