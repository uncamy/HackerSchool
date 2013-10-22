#my first socket! 
#Hacker School 10/21/13

import socket

server = socket.socket()
server.bind(('', 7777)) #operating system allow people to connect
server.listen(10) 

peeps = []

server.setblocking(False)
while True:
    try:
        c, (ip, port) = server.accept()
    except socket.error: #catches setblocking errors
        pass
    else:
        print 'We have a connection' 
        peeps.append(c)
        c.setblocking(False)
    for person in peeps:
        c.recv()
        c.send() 

c.select # is the right way to do it
 
