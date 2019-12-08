#                   判  断
'''
apple=int(input("请问你要买多少斤苹果："))
#  如果你买的苹果，重量10斤以内，那么价格单价就算5块。
#   如果买的苹果总量在10斤以上，20斤以内，按单价4元
# 如果大于10斤，那么单价就是3.56块。
if apple<=10:        #  if 是 如果  的意思
    print("总共价格是：",apple*5,"元 ")
elif apple>10 and apple<=20:
    print("总价格是：",apple*4,"元")     
else:             
    print("总共的价格是;",apple*3.5,"元")


#            in 的用法  （在不在）
x="今天天气还可以"
if "天" in x:       #  in 是： 在不在  ，if 是：如果，  else 是: 其他
    print("在里面")
else:
    print("不在里面")


    #  is 的用法  (是 的意思)   
x1=10
if type(x1) is int:     # type 获取用户类型  ，int 整数的意思
    print("是数字")
else:
    print("不是数字")


#          如果判断字典里面的1是 字符还是 整数，怎么写？
zidian={
    "xx":1,
    "yy":"2",
    "cc":True,
    "zz":None,
    "ss":2.333,
    "ff":"浪晋的测试小讲堂",
    "ww":[],
    "pp":(),
    "oo":{},
    "key":None,
}
for i in zidian:     
    if type(zidian[i]) is int:    #  type 判断类型 ,int 是 整数。
        print("key为",i,"的这个值的类型是",type(zidian[i]))
    elif type(zidian[i]) is str:   # str 是 字符串
        print("key为",i,"的这个值的类型是",type(zidian[i]))
    elif type(zidian[i]) is float:   # flot 是 浮点型
        print("key为",i,"的这个值的类型是",type(zidian[i]))
    elif type(zidian[i]) is list:   # list 是 数组
        print("key为",i,"的这个值的类型是",type(zidian[i]))
    elif type(zidian[i]) is tuple:   # tuple 是 元组
        print("key为",i,"的这个值的类型是",type(zidian[i]))
    elif type(zidian[i]) is dict:   # dict 是 字典
        print("key为",i,"的这个值的类型是",type(zidian[i]))
    elif type(zidian[i]) == "NoneType":   # "NoneType" 是空，不存在 
        print("key为",i,"的这个值的类型是",type(zidian[i]))
    elif type(zidian[i]) is bool:   # bool 是 布尔值
        print("key为",i,"的这个值的类型是",type(zidian[i]))
    else:
        print("不知道是什么类型!")
   

#   练习：有一数组[12,34,56,67,43,66,57,86,78,56,76,4,78,65,3,121,23,7,878,87,34,44]  
#    1. 找出87的下标
#    2.把数组以60为界限，拆成两个不同的数组
#    3.对数组从小到大进行排序

x2=[12,34,56,67,43,66,57,86,78,56,76,4,78,65,3,121,23,7,878,87,34,44]
x3=x2.index(878)    # index 是获取某个值的 下标
print("878的下标是：",x3)


haix2=[]
lowx2=[]
for i in x2:
    if i >=60:
        haix2.append(i)
    else:
        lowx2.append(i)
print(haix2,lowx2)    

for i in range(len(x2)):
    for j in range(len(x2)):
        print(x2[i],x2[j])



print(".........................................")
#   新课
x={1:"2",2:"hhh",3:"哈哈"}
x["18"]="哈哈哈"
print(x)
del x[1]
print(x)
print("............")


a=input("请输入你的名字： ")
b=input("请输入你的年龄： ")
c=input("请输入你的爱好： ")
xx="大家好，我叫{}, 我年龄是{} , 我的爱好是{}" . format(a,b,c)
print(xx)



xxx=int(input("请输入你的年龄： "))
if xxx>50:
    print("退休享受生活啊！！")
elif 23>xxx>18:
    print("生活的艰辛需要你咬牙前行！")    
elif 18>xxx>10:
    print("上学好好读书！")    
else:
    print("好好想想社会的残酷啊")   
print(".........................................")

 
#                              (题目)    写发红包的代码
hbao=input("请输入红包金额: ")
for i in hbao:
    if i not in "0123456789.":  # 如果不在"0,1,2,3,4,5,6,7,8,9,."范围内
        print("输入的值不合法，请输入数字金额")
        exit()
xx=hbao.count(".")      # 控制红包金额的小数点只能有一个
if xx>1:
    print("该输入的值不合法")
else:
    if "." in hbao:
        yy=hbao.index(".") + 1   # 获取 “.”的下标位置
        zz=len(hbao)
        floatlen=zz - yy
        if floatlen > 2:            #  发红包的金额数值不能超过两位。
            print("只留2位小数！")
        else:    
            hbao=float(hbao)
            if hbao>=0.01 and hbao<=200:
                print("红包发送成功,红包金额{}".format(hbao))
            else:
                print("红包发送失败,{}不在范围内".format(hbao)) 
    else:
        hbao=float(hbao)
        if hbao>=0.01 and hbao<=200:
            print("红包发送成功,红包金额{}".format(hbao))
        else:
                print("红包发送失败,{}不在范围内".format(hbao))    
'''  

'''
                           作业：
1、请用python打印出99乘法表。
2、有这么一个数组,[34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56],请以100为分界线，讲小于等于100的放到一个新数组中，将大于100的放到另一个新数组中。
3、重新自己实现一遍，我们课堂上讲的【发红包】功能。
4、输入某年某月某日，判断这一天是这一年的第几天？
5、有一个5 位数的任意数字，请将数字的顺序颠倒。（不是长的像数字的字符串哦）
'''

#    1、请用python打印出99乘法表。

============     第一种：使用for遍历循环嵌套      ===========================
for i in range(1,10):              # 如for i in range （1,10）的意思就是把1,2,3,4,5,6,7,8,9依次赋值给i
    for j in range(1,i+1):#当i = 2，j=(1,3)，此时j 的取值就是1，2
                          #当i = 3，j=(1,4)，此时j 的取值就是1,2,3
                          #当i = 4，j=(1,5)，此时j 的取值就是1,2,3,4
        print(i,"*",j,"=",i*j,end=" ")   # 其中end = “ ”的意思就是在每个计算的结尾处加个空格。
    print( )

print("==============================================")

# ==============第二种：使用for遍历嵌套while循环   ================


for x in range(1,10):
    y = 1
    while y<=x:
        print("%s*%s=%s" % (x,y,x*y),end = " ")    # %s*%s=%s" 是初始化
        y +=1
    print()


# 有这么一个数组,[34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56],请以100为分界线，讲小于等于100的放到一个新数组中，将大于100的放到另一个新数组中。
a = [34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56],