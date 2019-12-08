# 九九乘法表
# #  for 循环
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"*",j,"=",i*j,end="  ")
#     print( )



#  while 循环
for x in range(1,10):
    y = 1
    while y<=x:
        print("%s*%s=%s" %(x,y,x*y),end = "  ")
        y +=1
    print( )