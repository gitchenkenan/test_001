# -*- coding: utf-8 -*-
import json
import os

files = os.listdir("..\\test_data\\")

dict1 = {}
for i in files:
    if os.path.splitext(i)[1] == ".json":
        print os.path.splitext(i)[0]
        new_path = os.path.join("..\\test_data\\",i)
        with open(new_path,"r"):
            dict1[os.path.splitext(i)[0]] = open(new_path,"r").read()

print dict1