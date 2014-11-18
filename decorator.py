#coding:utf8


#装饰器函数

#木有参数的装饰器函数
def deco_check(f):
    if f.__doc__ == None:
        print("我操!")
    else:
        print("我不操了")

    return f  #一定要返回装饰后的对象

@deco_check

def f():
    "This is a __doc__"
    print('welcome to my home')

f()

#带有参数的装饰器
def sum(x):
    def trueSum(s):  #这个才是真的内部装饰函数
        print(x*5)
        return s
    return trueSum

@sum(20)
def s():
    print('ok')
s()
