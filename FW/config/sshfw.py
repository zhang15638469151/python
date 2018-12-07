#!/user/bin/python
#-*- coding:utf-8 -*-
#Author:一土小亘兄
#@Time: 17:44
import paramiko
###链接fw后台，括号中输入命令返回结果
def sshfw(mingling):
    ssh = paramiko.SSHClient()  ###先创建一个ssh客户端
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  ####允许链接不在know_hosts文件中的主机
    ssh.connect(hostname='30.1.1.1', port=22, username='root', password='N@9!0~6$Bane3')
    stuin, stuout, stuerr = ssh.exec_command(f'{mingling}')  ###exec_command()  括号中写执行的命令
    result = stuout.read()  ###读取结果，结果类型是bytes
    relice = result.decode()
    return relice
