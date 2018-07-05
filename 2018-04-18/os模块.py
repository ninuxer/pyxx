# Author： ninuxer
# Date： 2018/04/18 14:13
# File： os模块.py


import os


# os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd
# os.curdir  返回当前目录: ('.')
# os.pardir  获取当前目录的父目录字符串名：('..')
# os.makedirs('dirname1/dirname2')    可生成多层递归目录
# os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove()  删除一个文件
# os.rename("oldname","newname")  重命名文件/目录
# os.stat('path/filename')  获取文件/目录信息
# os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# os.linesep    输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
# os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:
# os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# os.system("bash command")  运行shell命令，直接显示
# os.environ  获取系统环境变量
# os.path.abspath(path)  返回path规范化的绝对路径
# os.path.split(path)  将path分割成目录和文件名二元组返回
# os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)  如果path是绝对路径，返回True
# os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
# os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
# os.path.getsize(path) 返回path的大小


print(os.getcwd())
# os.chdir(r'C:\Windows\System32\drivers\etc')
print(os.getcwd())

print(os.curdir)
print(os.pardir)



os.makedirs('tasks\job1\job2\job3')
print(os.listdir(os.getcwd()))

os.removedirs('tasks\job1\job2\job3')

# os.remove('tofile')

# os.rename('test','testbynwc.txt')

print(os.stat('testbynwc.txt'))

import time
print(time.strftime("%F_%T",time.localtime(os.stat('testbynwc.txt').st_atime)))

print(os.sep)
print(os.linesep.isprintable())
print(os.pathsep)
print(os.name)

# os.system(r'date')


print(os.environ)



# os.path相关

print(os.path.abspath(r'gen\root\sss\aaa\ccc\ddd.txt'))

print(os.path.split(r'gen\root\sss\aaa\ccc\ddd.txt'))


print(os.path.dirname(r'gen\root\sss\aaa\ccc\ddd.txt'))

print(os.path.basename(r'gen\root\sss\aaa\ccc\ddd.txt'))

print(os.path.exists(r'gen\root\sss\aaa\ccc\ddd.txt'))

print(os.path.isabs(r'D:\aaa\bbb\ccc'))

print(os.path.isfile(r'D:\工作相关文档\python-study\oldboy\2018-04-18\func1.py'))

print(os.path.isdir(r'D:\工作相关文档\python-study\oldboy\2018-04-18'))

print(os.path.join('aaa','bbb','ccc.aa','ddd'))

print(os.path.getatime(r'D:\工作相关文档\python-study\oldboy\2018-04-18\testbynwc.txt'))
print(os.path.getmtime(r'D:\工作相关文档\python-study\oldboy\2018-04-18\testbynwc.txt'))
print(os.path.getctime(r'D:\工作相关文档\python-study\oldboy\2018-04-18\testbynwc.txt'))
print(os.path.getsize(r'D:\工作相关文档\python-study\oldboy\2018-04-18\testbynwc.txt'))
