#coding:utf8


#join()方法 字符.join(序列,[元组])

str = ['hello','python']

print(str)

new = '|'.join(str) #生成一个字符串

print(type(new)) #str类型


#序列方法reverse(反转) / sorted(排序)  /sum(相加)

lis = [1,2,3,4,5]

print(sum(lis)) #输出 15

print(lis.reverse()) #why None


#序列的拷贝 引入copy模块

import copy

newLis = copy.copy(lis)

print(newLis)
