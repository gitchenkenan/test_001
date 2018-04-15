# -*- coding: utf-8 -*-
import json
import os
import string


class JsonFileData():
    def get_json_data(self):
       dict1 ={}
       dir = "..\\test_data\\"
       for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                if filename.endswith('.json'):
                    with open("..\\test_data\\"+filename) as file:
                        dict1[filename.split(".")[0]]= file.read()
            return dict1



