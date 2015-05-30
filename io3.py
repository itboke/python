
#--------------
try:
	f = open('./1.txt','r')
	print f.read()
except error,e:
	print 'error',e

finally:
	if f:
		f.close()