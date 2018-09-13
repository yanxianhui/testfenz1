import requests
import json
class Interface_test:
    def __init__(self,url,method,data=None,headers=None,json=None):
        self.res =self.run_main(url,method,data,headers,json)
    def send_get(self,url,data,headers,json):
        res = requests.get(url=url,data=data,headers=headers,json=json)
        t = res.json()
        return t
    def send_post(self,url,data,headers,json):
        res = requests.post(url=url,data=data,headers=headers,json=json)
        t=res.json()
        return t
    def run_main(self,url,method,data=None,headers=None,json=None):
        res =None
        if method =='get':
            res = self.send_get(url,data,headers,json)
        else:
            res=  self.send_post(url,data,headers,json)
        return res
if __name__ == "__main__":
     #url = 'http://www.clearbos.cn:82/api/auth/login/checklogin'
    #data = {
     # 'userAccount': '15890158362',
     # 'userPassword': '123456',
    #}
   #url = 'http://www.clearbos.cn:82/api/auth/menu/getmenu?userAccount=15890158362'
   #headers = {
      # 'Authorization': 'Bearer ' + 'PMQcvObb2mq-PQ4V5royZDbxg6NZsjUx0P4blaabRsDQVkWIkVgRUpZXQweQoFYcVypZkBnotXHz1vZbqYB8W3rdtEKK1MGRvF5-GZ5C5of4hQsGBR59eTEtpqNdcqXcm43PAxnvy-TsoPWPUQVk9FUWFU62mcR-rHrW_ONJ6aGhambW_jC-CgCtSQyiaHpkyFYC9RjzLq2phNVy0Ph9DrUNny-Pdew33GhQQ0y8kT35fNUfN44LqLoj18AKejudHgTW5YPZgvEx2Bh-34uVaw',
    # }
   # run=Interface_test(url, 'GET',data)
    #print (run.res)
     url='http://www.clearbos.cn/SimpleEMRServices.ashx'
     data={
         "operationType": "NewErmCode"
     }
     run = Interface_test(url, 'post', data)
     print (run.res)
    #Interface_test()