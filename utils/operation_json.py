# -*- coding: utf-8 -*-
import json
class OperetionJson:
	def __init__(self,file_path=None):
		if file_path  == None:
			self.file_path = '../data/user.json'
		else:
			self.file_path = file_path
		self.data = self.read_data()

	#读取json文件
	def read_data(self):
		with open(self.file_path,encoding="utf-8") as fp:
			data = json.load(fp)
			return data


	#根据关键字获取数据
	# def get_data(self,id=None):
	# 	#print (type(self.data))
	# 	return self.data[id]
	def get_data(self,id=''):
		res=None
		#print (type(self.data))
		if id=='':
			res=None
		else:
			res=self.data[id]
		return res

	#写json
	def write_data(self,data):
		with open('../data/cookie.json','wb') as fp:
			fp.write(json.dumps(data))


if __name__ == '__main__':
	opjson = OperetionJson()
	print (opjson.get_data('SHOUJU'))
    #print(OperetionJson.get_data('user'))

