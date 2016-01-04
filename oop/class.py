# -*- coding:utf-8 -*-  
class Person(object):
	__name = "hello,world"
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def print_info(self):
		print("%s ---- %s" % (self.name.decode('utf-8'),self.age))

obj = Person('黄泽淋','24')
obj.print_info()

		