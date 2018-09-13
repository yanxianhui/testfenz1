from utils.HTMLTestRunner import HTMLTestRunner
from test.tes_zidong import TestJieKou
from utils.config import Config, DRIVER_PATH, DATA_PATH,REPORT_PATH
import time
from utils.mail import Email
if __name__ == '__main__':
    #now = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
    report = REPORT_PATH + '\\report.html'
    #print(report)
    with open(report, 'wb+') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='ERP测试报告', description='修改html报告')
        runner.run(TestJieKou('test_search'))

    e = Email(title='ERP测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='825651673@qq.com',
              server='smtp.126.com',
              sender='luckyanhui@126.com',
              password='yan986165220',
              path=report
              )
    e.send()
