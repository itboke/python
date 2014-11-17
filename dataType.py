#coding:utf8

#序列类型的数据类型：列表、元组、字符串

#列表的定义:[元素1,元素2,....] 通过索引下标来引用

list = [1,2,3,4,'python','helloworld']

#通过列表的append(item)向列表后面添加元素

print(list[4]); #输出的是python

list.append('beautyful');

print(list);#输出[1, 2, 3, 4, 'python', 'helloworld', 'beautyful']


#元组(tuple) 和列表的一些方法

t = (1,2,3) #定义元组

#len()  获取元素的长度

print(len(t)); # 3 


#del() 删除元素 ， 不能删除元组的元素，可以删除列表的元素

del(list[0]); # 删除了 1

print(list)

#切片方法(slice) 获取元组或者列表的元素组成的子集,通过[开始下标:结束下标]来获取
print(t[1:3]) #获取到[2,3]

#in关键词  3 in [1,2,3] 判断元素是否存在元组或者列表中
if 3 in t:
    print('存在')
else:
    print('不存在')


#''' 字符串内容 '''   '''..'''长字符串类型
str = '''
    <html>
          <head></head>
          <body></body>
    </html>
'''
print(str) #按原格式输出

#字典数据类型，相当于js的对象格式或者JSON格式{"name":"python","version":3.3.2}
#它是一组hash值

isHash = {"name":"helloPython","version":3}
print(isHash);

#dict(key) 获取字典中key的值
print(isHash["name"]) #输出helloPython

#判断key是否存在字典中
print("name" in isHash)

#异常处理
demo = {"name":"python"}
try:
    demo['age']
except:
    print(" The key in not ready")
else:
    print("no error")


#def关键字定义一个函数

def echoYourName(name):
    print(name)

#调用函数echoYourName
echoYourName('my name is python!')


    
