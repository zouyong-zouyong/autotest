# # post 方法的 demo 的
# import requests

# # json: 字典格式
# url ="http://132.232.44.158:5000/userLogin/"   #接口地址
# data = {"username":"test", "password":"test", "captcha":"123456"}   # 传递数据： 字典格式

# # 单等号 左边的 都是一个变量
# res = requests.post(url=url,json=data)  # 向 erl接口使用post方法传递data的json数据
# print(res.text)



                      # 第二天的复习
# post 方法的 demo
import requests

#  json : 字典格式 
url = "http://132.232.44.158:5000/userLogin/"   #  接口地址
data = {"username":"test", "password":"test", "captcha":"123456"}  # 传递的数据:字典格式


res = requests.post(url=url,json=data)   # 向 URL 接口使用 post方法 传递data的 json 数据
print(res.text)


# form -data 推荐用postman 生成代码的方式来实现
# requests02.py