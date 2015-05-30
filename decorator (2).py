
import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		
		print 'call begin %s():' % func.__name__
		
		
		func(*args,**kw)
		
		
		print 'call end'
					
	return wrapper



@log  # now = log(now)
def now():
	print '2015-05-12'
	
now()	

print now.__name__


	
		