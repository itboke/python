#coding:utf8

#列表解释和生成器迭代

[y for y in range(20) if y % 2 == 0]


#生成器迭代

result = (s for s in range(2,20) if s % 3 == 0)
