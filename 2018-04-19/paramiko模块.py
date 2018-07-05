# Author： ninuxer
# Date： 2018/04/20 10:30
# File： paramiko模块.py

## 通过ssh远程执行命令
# import paramiko
#
#
# ssh = paramiko.SSHClient()
#
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('10.200.11.110','22','root','1q2w3e,./')
# stdin,stdout,stderr = ssh.exec_command('df -h')
# print(stdout.read().decode())
# ssh.close()

## 通过sftp上传下载文件
# import paramiko
# t = paramiko.Transport(('10.200.11.110',22))
# t.connect(username='root',password='1q2w3e,./')
# sftp = paramiko.SFTPClient.from_transport(t)
# sftp.put('application.ini','/tmp/application.cfg')
# sftp.get('/root/flume.sh','flume.bat')
# t.close()


## 以上两个都可以基于秘钥完成，但是windows没有秘钥，故没有验证

