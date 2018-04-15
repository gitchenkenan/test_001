# -*- coding: utf-8 -*-
import requests


class HttpRunner():

    def __init__(self,url,types,data=None):
        self.headers = {"Content-Type": "application/json"}
        self.url = url
        self.data = data
        self.types = types

    def post_data(self):
        result = None
        if self.types == "POST":
            result = requests.post(url=self.url,data=self.data,headers=self.headers)
        elif self.types == "GET":
            result = requests.get(self.url,self.data)
        return result.json()



if __name__ == "__main__":
    url = "http://www.sojson.com/open/api/weather/json.shtml?city=北京"
    result = HttpRunner(url,"GET").post_data()
    print result