#1）  print（普任特）：是打印，输出。

#2）  字符串
print("你好，我是邹勇！") #只要是 "字符串" 都要加“”或''单双引号，只要加“”双引号都是“字符串”，不管双引号里面是什么内容

#3）  浮点型
print(2333) #是整数类型
print(2.333) #是小数类型
#第2和3行都属于 “浮点型” ，整数不用加""双引号;

#4）  变量 和 赋值
haha=23333
print(haha)
# 将 2333 赋值给变量 haha 
#（变量分为私有和公有，目前私有没教）

#5） 获取数据类型-- type(太普)。（其结果共有两种：int 和 false）
print(type(23333))
#输出是 int。  int（应特）是：整数的意思。

print(type(2.3333))
#输出是 float。  float（服楼特）是：小数或浮点数的意思

# “布尔值”类型比较特殊，用于“判断”类。
# 布尔值（bool）有true(处)  和   false(服来斯)两种。
print(1==1)  # 输出为true  “对”，1等于1.
print(1==2)  # 输出为false  “错误”，1不等于2.
# true(处)：对，成功的意思。  
# false(服来斯)：错，失败的意思。


#空（None type）代表：不存在的意思，就一个值 None(浪)，。
#  Nonetype（浪太傅）：空类型的意思
a=None
print(a)  #输出结果为None，空。空类型（None）与空格是不同的。

#元组（tuple——腿破）：由一个（）小括号组成。()括号里装一些如：（1，2，3，4，"哈哈"，）等数据。
yuanzu=(1,2,3,4,"haha")
print(yuanzu)

#下标  在元组里取下标。（下标一般从“0”位开始计数，如有8位数，则范围是从0-7内。）
yuanzu=(1,2,3,4,"haha")
print(yuanzu[3])  #输出结果为"4",输出打印里的[]中括号是 固定的 ，不能写成的别的符号。

#在元组里选取多个不同的下标 或 连续的下标。
yuanzu=(1,2,3,4,"haha")
print(yuanzu[0],yuanzu[2],yuanzu[4]) #输出结果：1 3 haha
print(yuanzu[2:4]) # 输出内容是第2个到第4个 ，输出结果： (3, 4）。
print(yuanzu[-2])  # 输出结果：4.


#元组有两个方法：count（康肯特）和index(应弟克丝)。
#元组一旦定义好了，就不能修改。
#index(应弟克丝)：在元组里找“下标”数据
yz=(1,2,3,4,5,6,7,8,9)
xiabiao=yz.index(3)   #()括号里不加“”双引号。
print(xiabiao)  #输出结果是：2，表示 3 在元组里是第2个下标。

# count(康肯特)：用于统计。
yz=[1,2,5,4,5,6,7,8,5]
xiabiao=yz.count(5)
print(xiabiao) #输出结果是：3，表示5在元组里有3个。

# 数组 list（累死特）：和元组一模一样，用[]用中括号表示，个别地方叫“列表”。
# 数组和元组的不同之处在：数组能修改，元组不能修改。


#在数组里插入数据
shuzu=[1,2,5,4,5,6,7,8,5] #数组必须用[]中括号表示
print(shuzu)
shuzu.append("新插入的数据")
print(shuzu)  # 输出结果：在数组末尾加入了“新插入的数据”，[1, 2, 5, 4, 5, 6, 7, 8, 5, '新插入的数据']

#字典 dict(爹科特)：用花括号{}表示。
# 字典无 “下标”，#键值对
zidian={0:10,"name":"邹勇",5:1111,11:"最终结果"}
print(zidian[5])  #打印输出 zidian 后面只能接[]接中括号，不能接{}花括号。


print(None)    #输出结果  None  空
print(" ")     # 输出结果  没有，  代表 空格键











git config --global user.name "zouyong-zouyong"

git config --global user.email "2550577200@qq.com"
ssh-keygen -t rsa -C "2550577200@qq.com"