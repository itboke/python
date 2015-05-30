
#-------------

f = open('./1.txt','r')
datas = f.readlines()

for i in datas:
	print i.strip()