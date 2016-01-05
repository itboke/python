# -*- coding:utf-8 -*-  
class Person(object):
	#定义静态属性 private变量
	__name = "hello,world"
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def print_info(self):
		print("%s ---- %s" % (self.name.decode('utf-8'),self.age))

	#公共方法 访问 类静态属性	
	def print_static(self):
		print("%s------" % (self.__name))

#obj = Person('黄泽淋','24')
#obj.print_info()
#obj.print_static()

# 继承 继承有什么好处？最大的好处是子类获得了父类的全部功能
class Animal(object):
	#限制该class实例能添加的属性      
	__slots__ = ('name','age')
	"""docstring for Animal"""
	def run(self):
		print("runing in road")

#创建一个dog类 继承 Animal
class Dog(Animal):
	pass

bb = Dog()
bb.run() # print 'runing in road'


# 获取对象的信息
# (1) 判断对象的类型 使用type()判断
print(type("hello"))
# (2) isinstance() 判断 一个对象是否是某种类



		
		
		