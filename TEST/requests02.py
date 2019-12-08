import requests

url = "http://132.232.44.158:8080/morning/user/userLogin"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginName\"\r\n\r\n123@qq.com\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginPassword\"\r\n\r\na123456\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'Postman-Token': "d0e42289-94b9-4636-8332-dbd6ea562921"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print("响应值是"response.text)



#  如何做接口测试   
#  0----构造需求
# 1.判断hppt状态码
a = response.status_code   # 返回值的http状态码
assert a ==200            # 断言http响应值是否等于200


print("htto响应状态码的断言通过了")
# 2.和接口文档对比判断响应值
b = response.json
assert b ["success"] ==True    #断言返回值success是否为True
print("响应值断言通过！")


# 3.再判数据库后台与前台文档数量和内容是否一致。
