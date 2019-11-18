# 01  类==============================必须要掌握的================

# 
'''
#普通的变量
 a = [1,2,3]
 b = 1
 c =  True
'''


# 普通办法
def ccc():
     print("12312312")
# ==========================================================================


                    #   class 01
#  类包含了属性（特征）和方法（行为，能干啥）
# 类名字首字母大写
class person():
     # 成员变量。无论哪一个地方都能用成员变量
    mz = "海贼王"
    nl = 48
    sg = 178                                   #就是说，成员方法，就是在类里面要引用就是用self指代，在类外面用的时候，直接用定义的实例化去指代呀，是这样嘛。
    xb = "男"

    # 成员方法：已self参数开头的方法
    #类本身的实例化对象
    def haha(self):              #  haha 可以随意取值
        print("大家好，我是长达两年半的实习生，我会玩游戏")
        print("还有谁")
        print("还有篮球")
        
    #成员方法的传参
    def tiao(self,wd):      #  def 是一个方法关键字        wd = "小苹果"
        print("我会跳{}".format(wd))

    # self的用法
    # self：和类本身的实例化对象一样 。   self在类里面用： 实例对象在类外面
    def rap(self):
        a = self.mz             #引用类的属性
        print(a)               #
        self.haha()             #引用类的成员方法


#实例化:p是person的实例化对象
#引用类，不要放到类里面去
d = person()                #赋值语句
print(d.mz)                 #引用类的成员变量
d.haha()                    #引用类的成员ff
d.tiao("小苹果")             #成员方法分传参

d.rap()                 # self 在类里面引用变量的方法

#= = = = = = = = = = 必须要掌握 （背） = = = = =  = = = = = = = = 


#引用类的成员变量
print(d.mz)     
print("........................................")






#=============================进阶：掌握==================================
#  类的构造方法   、 2.类的继承



class person():
    name = "海贼王"
    sex = "男"



    #构造方法：固定方法：初始化类的
    def __init__(self,xb,mz):
        self.sex = xb
        self.name = mz
        self.test()

    def test(self):
        print("这是test的方法")

d = person("女","海贼王")
print(d.sex)
print(d.name)




# #=============================进阶：掌握
# #  类的构造方法   、 2.类的继承



# class person():
#     name = "海贼王"
#     sex = "男"



#     #构造方法：固定方法：初始化类的
#     def __init__(self,xb,mz):
#         self.sex = xb
#         self.name = mz
#         self.test()

#     def test(self):
#         print("这是test的方法")

# d = person("女","海贼王")
# print(d.sex)
# print(d.name)








# # 类的继承
# #重写
# print("..........................")
# class Dongwu():
#     tz = 100

# def run(self):
#     print("动物能跑！")

# class ren(Dongwu):
#     pass                 #占坑。语法不会报错，啥也不是
#     tz = 200
#     def run(self):
#         print("人能跑！")

# r = Ren()          
# print(r.tz)
# r.run()             