#   for 循环
#   range 是一个数列生成器
#  end是排版，”“双引号里加空格键，排版就越开

xx=range(90,98)  # range 是一个数列生成器
#(90,98)左闭右开，90-97，没有98

print(list(xx))

for i in xx:    # i 是 index的意思 
    print("第",i,"次循环 ")

for i in range(100):
    print("我好饿") 



#             用 for 写出99乘法口诀
for i in range(1,10):    
    for j in range(1,i+1):   #左闭右开，不会到10
        print(i,"*",j,"=",i*j,end="   ")  #  end是排版，”“双引号里加空格键，排版就越开
    print()     #这个不能少，排版成一行行的

zidian={
    "a1":"111",
    "a2":"222",
    "a3":"333",
    "a4":"5466",
    "a5":"666"
    }
for i in zidian:
        print(zidian[i])


a=1
while a<10:   #设定条件，结果必须在10以内，
    print("哈哈哈1")    #计算结果在10以内就输出  “哈哈哈
    a=a+2               #计算结果是a+2在10范围内输出 ”哈哈哈“，超出不显示



#        for循环，计算从 1加到100 的结果
x=0
for i in range(1,101):   # 设定条件，1到101的范围内计算
    x+=i        #起变化，计算X+1+2+。。。。一直加到100
print(x)

y=0
while y<10:
    print(y)
    y=y+1

