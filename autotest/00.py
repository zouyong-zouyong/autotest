# #  类
# class hhh():
#     mz = "海贼王"
#     nl = 24
#     sg =175
#     def haha(self):
#         print("大家好，我是实习生，我会玩")
#         print("我会跳")    
#         print("我会叫") 
#         print("我会唱") 

#     def hh(self,wd):
#         print("大家好，我叫{}".format(wd))

#     def rap(self):
#         c = self.nl
#         print(c)
#         self.haha()

# d = hhh()
# print(d.mz)
# d.haha()
# d.hh("小苹果")
# d.rap()


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
class aaa():
    mz = "路飞"
    mx = "当海贼王"

    def  __init__(self,xb,hh):
        self.mx = xb
        self.mz= hh
        self.text()
    def text(self):
        print("这是text的方法")

cc = aaa("当海军","女")
print(cc.mx)
print(cc.mz)