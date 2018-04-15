# -*- coding: utf-8 -*-
import json


class OperatingJsonFile():

    #构造方法
    def __init__(self,file):
        # self.data = self.read_json_data(file)
        self.file = "..\\testdata\\%s"%(file)

    def get_json_data(self):
        return self.read_json_data()

    #读取json文件数据

    def read_json_data(self):
        with open(self.file) as f:
            # print f.read()
            return f.read()


if __name__ == '__main__':
    oj = OperatingJsonFile("create_license_forA.json")
    print oj.get_json_data()