import socket
localIP = socket.gethostbyname(socket.gethostname())#
print "local ip:%s "%localIP


ipList = socket.gethostbyname_ex(socket.gethostname())[2]
for i in ipList:
    if i != localIP:
       print "external IP:%s"%i