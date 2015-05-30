#coding:utf-8
#oop 
class Student(object):
	
	def __init__(self,name,age):
	
		self.__name = name
		self.__age = age
		
		
	def get_name(self):
		print self.__name
	
	def get_age(self):
		print self.__age
	
	def set_name(self,name):
		self.__name = name
		
	def set_age(self,age):
		self.__age = age


me = Student('python',100)

me.get_name()
me.get_age()

me.set_name("emituofo")
me.get_name()

#print me._Student__name 