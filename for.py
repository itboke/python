
from collections import Iterable  #judge a data isn't a Iterable

info = { 'name':'python','couontry':'japan','age':20}

for key in info:# key
	print key
	

for value in info.itervalues():# value
	print value
	

for k, v in info.iteritems():#key and value
	print k,v
	



print isinstance('123',Iterable) #true 


lists = [1,2,3,4]

aaa = enumerate(lists);

for k, v in aaa:#index and element
	print k,v

