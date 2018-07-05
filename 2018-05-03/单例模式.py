# Author： ninuxer
# Date： 2018/05/04 14:25
# File： 单例模式.py


# 单例模式就是指某个类实例化出来的对象始终是同一个，这样就可以节约避免创建多个不同的对象造成的资源浪费
# 应用场景：如创建一个数据库连接池的对象，此后所有需要调用数据库连接的，都是使用同一个连接池对象

class P:
    def __init__(self,ip,port,user,pwd,db):
        self.ip = ip
        self.port = port
        self.user = user
        self.password = pwd
        self.database = db
        self.poolsize = 30

    __instance = None   # 单例模式的获取对象的定义示例

    @classmethod
    def get_instance(cls):  # 单例模式的获取对象的定义示例
        if cls.__instance:
            return cls.__instance
        else:
            ip = input("IP is : ")
            port = input("PORT is : ")
            u = input("USER is: ")
            p = input("PASS is: ")
            d = input("DATABASE is: ")
            cls.__instance = cls(ip,port,u,p,d)
            return cls.__instance

    def caozuo(self):
        print(self.ip)
        print(self.port)
        print(self.user)
        print(self.password)
        print(self.database)
        print(self.poolsize)
        print('其他操作')

# 单例模式创建对象不再使用 类(xx)的方式，而是要用类中定义的获取对象的方法

obj1 = P.get_instance()
print(obj1)
obj2 = P.get_instance()
print(obj2)
obj3 = P.get_instance()
print(obj3)

obj2.caozuo()