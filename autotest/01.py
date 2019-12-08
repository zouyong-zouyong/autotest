 #  类  面向对象

class Car:
    def __init__(self,lunzi,yanse,moshi,zuowei):   #定义一个方法
         # def 是定义一个方法或函数.
         #   __init__是:(初始值)传入方法，该代码是固定的不可更改和替换
        self.lunzi=lunzi
        self.yanse=yanse
        self.moshi=moshi
        self.zuowei=zuowei
        #self指的是类实例对象本身(注意：不是类本身)。

    def run(self,x):  #run方法并不启动，就是在主线程里调用一个函数而已。
         print(self.zuowei,"车跑起来了！")  #功能代码
         print("这是类里面的方法传入的变量",x)
           
    def zhuting(self):
        print("车正在驻停中！")


car=Car(3,"红色","油电混合","6座")  #类的实例化
lunzi=car.moshi
print(lunzi)

car.run("哈哈哈")
car.zhuting ()

    