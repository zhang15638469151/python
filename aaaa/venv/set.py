#服务器端server（tcp）
import socket
#创建socket,封装协议（ipv4协议，tcp协议）
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP和端口号(bin接受到的参数是元组)
host = ('192.168.0.81',5555)
# 三种IP地址可填写
# 本机IP     环回地址（127.0.0.1）
# 0.0.0.0（所有IP）
s.bind(host)
#监听(括号里只能是数字:指的是最大等待数)
s.listen(3)
while True:
    a,b = s.accept()   #接收请求，accept执行后有两个结果，第一个结果a是客户端的连接信息，第二个结果b是存放的是客户端的IP地址和端口号
    msg = a.recv(1024)       #1024代表每次接受的最大字节数
    print(msg.decode('utf-8'))
    #发送响应
    reg = 'welcome'
    a.send(reg.encode('utf-8'))










#服务器端server（udp）
import socket
#创建socket,封装协议（ipv4协议，udp协议）
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定IP和端口号(bin接受到的参数是元组)
a = ('192.168.0.81',5555)
s.bind(a)
while True:
    a,b = s.recvfrom(1024)      #接受数据  产生两个变量，第一个变量：客户端发送的请求数据，第二个变量：客户端的IP地址和端口号
    print(a.decode('utf-8'))
    print(b)
    #发送响应数据
    msg = input('>>>')
    s.sendto(msg.encode('utf-8'),b)











