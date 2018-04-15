# -*- coding: utf-8 -*-
from tools.http_runner import HttpRunner
import json
from tools.json_file import JsonFileData
import HTMLTestRunner
import unittest
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


class LicenseFunc():
    # 删除产品license
    def license_delete(self,license_id):
        url = "http://47.92.88.246:8999/it-license/it/license/delete"
        license_data = {"context": {"tenantId": "466","appId": "CRM", "userId": "1000"},"productLicenseIdList": license_id}
        result = HttpRunner(url, "POST",json.dumps(license_data)).post_data()
        print result

    # # 查询产品license
    # def license_query(self,tenant_id):
    #     url = "http://47.92.88.246:8999/it-license/it/query/license"
    #     data = {"licenseContext": {"tenantId": tenant_id,"appId": "CRM","userId": "1001","properties": {},"objectProperties": {}}}
    #     r = HttpRunner(url, "POST", json.dumps(data)).post_data()
    #     list_license = []
    #     for i in r["result"]:
    #         list_license.append(i["id"])
    #     return list_license

    # 查询modulelist
    def license_query_modulelist(self,tenant_id):
        url = "http://47.92.88.246:8999/it-license/it/license/module"
        data = {"licenseContext": {"tenantId": tenant_id,"appId": "CRM","userId": "1002"}}
        r = HttpRunner(url, "POST", json.dumps(data)).post_data()
        print r["result"]
        self.licenseid = r["result"]

    def license_update(self,tenant_id):
        url = "http://47.92.88.246:8999/it-license/it/license/update/info"
        json_data = JsonFileData().get_json_data()
        data = json_data["update_license"]
        print data
        data1 = json.loads(data)
        data1["context"]["tenantId"] = tenant_id
        print data1
        r = HttpRunner(url, "POST", json.dumps(data1)).post_data()
        print r

    #





# if __name__ == '__main__':


 # suite = unittest.TestLoader().loadTestsFromTestCase(LicenseFunc)
# filename = 'D:\mypython\ck-report.html'
# fp = open(filename, 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='report', description = 'unnitest测试报告')
# runner.run(suite)


#suite = unittest.TestLoader().loadTestsFromTestCase(unnit)
    # filename = '绝对路径'
    # fp = open(filename, 'wb')
    # HTMLTestRunner.HTMLTest(stream=fp, tile='report',description= '我的用例报告')
    #
    # runner.run(suite)
