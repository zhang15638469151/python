#tcp客户端
import socket
#创建socke，封装协议
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接服务器  接收到的参数是元组
soc.connect(('192.168.0.81',5555))
aaa = 'hi'
soc.send(aaa.encode('utf-8'))
#接收响应
msg = soc.recv(1024)
print(msg.decode('utf-8'))




#三种IP地址可填写
#本机IP     环回地址（127.0.0.1）
#0.0.0.0（所有IP）









#udp客户端
import socket
#创建socket,封装协议
soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#发送请求数据
a = ('192.168.0.81',5555)
while True:
    reg = input('>>>')
    soc.sendto(reg.encode('utf-8'),a)
    #接受响应
    c = soc.recv(1024)
    print(c.decode('utf-8'))

