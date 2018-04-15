# -*- coding: utf-8 -*-
import xlrd
import requests


class OperatingExcelFile():

    def __init__(self,file):
        self.file = "..\\testdata\\"+file

    def get_cell_value(self,x,y,sheet=0):
        table = self.get_table_data(sheet)
        return table.cell_value(x,y)

    def get_table_data(self,sheet=0):
        data = xlrd.open_workbook(self.file)
        table = data.sheet_by_index(sheet)
        return table

    def get_excel_data(self,sheet=0):
        table = self.get_table_data(sheet)
        #获取有多少行用例
        nrows = table.nrows
        #获取第一行的表头内容
        first_row_name = table.row_values(0)
        #定义一个list 来存储 每一行的内容
        data_list = []
        #取每一行的内容
        for rowNum in range(1,nrows):
            #获取每一行的内容
            row_value = table.row_values(rowNum)

            if row_value:
                row_data = {}
                #根据表头列数循环以表头列为字典的key值，行的每列的具体值为字典的value
                for i in range(0,len(first_row_name)):
                    row_data[first_row_name[i]] = row_value[i]
                data_list.append(row_data)
        return data_list

if __name__ == '__main__':
    o = OperatingExcelFile("testcase.xls")
    lists = o.get_excel_data()
    headers = {"Content-Type": "application/json"}
    url= lists[0][u"接口url"]
    # r = HttpRunner(lists[0][u"接口url"],lists[0][u"请求类型"],lists[0][u"请求参数"]).post_data()
    data = lists[0][u"请求参数"]

    r = requests.post(url,data,headers=headers)
    #print r.text