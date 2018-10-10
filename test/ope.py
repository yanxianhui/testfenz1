import unittest
from utils.file_reader import ExcelReader
from utils.config import Config, DATA_PATH,REPORT_PATH
from method.test_fen import Interface_test
from utils.operation_json import OperetionJson
from utils.HTMLTestRunner import HTMLTestRunner
from utils.log import logger

#写入实际结果
class TestJieKou(unittest.TestCase):
    excel = DATA_PATH + '/Sign.xlsx'

    def test_search(self):
        self.opjson = OperetionJson()
        datas = ExcelReader(self.excel).data
        succee = 0
        file = 0
        codeid = []
        for d in datas:
            with self.subTest(data=d):
                url = d['url']      #获取url数据
                method = d["Method"]      #获取请求类型数据
                datad=d['request']     #获取简化数据
                rely=d['relyon']
                jsonm=d['jsonn']
                data =self.opjson.get_data(datad)        #获取data数据
                headers=self.opjson.get_data(rely)      #获取data数据
                json=self.opjson.get_data(jsonm)
                run=Interface_test(url,method,data,headers,json)
                code=run.res
                #self.assertEqual(code['code'],'200')
                #print(code)
                #codeid.append(code['message'])
                try:
                     if code['message']==d['预期结果']:
                        succee+=1
                        links=' 通过 -    '+url,code
                        logger.info(links)
                        codeid.append('pass')
                     # if code['message']!=d['预期结果']:
                     #     file += 1
                     #     links = ' 失败 0-    ' + url, code
                     #     logger.info(links)
                     #     codeid.append('fail')
                     else:
                         file += 1
                         links = ' 失败 1-    ' + url, code
                         logger.info(links)
                         codeid.append('fail')
                except :
                   file+=1
                   links = ' 失败 2-    ' + url,code
                   logger.info(links)
                   codeid.append('fail')
                self.assertEqual(code['message'], d['预期结果'])
        gong = succee + file
        print("一共测试",gong,"条接口","成功",succee,"条","失败",file,"条")
        num = 1
        for add in codeid:
            num += 1
            value=str(add)
            print(value)
            ExcelReader(self.excel).write_value(num,8,value)
if __name__ == '__main__':
    #report = REPORT_PATH + '\\report.html'
    #with open(report, 'wb+') as f:
        #runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 灰蓝', description='修改html报告')
        #runner.run(TestJieKou('test_search'))
    TestJieKou('test_search')