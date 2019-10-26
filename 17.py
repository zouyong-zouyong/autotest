#                   判  断
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

