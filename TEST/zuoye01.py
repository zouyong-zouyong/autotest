# 作业
'''
1. 配置appium环境
2. requests：以lux项目的登录接口来做。
要求：定义变量存放用户名和密码 [["test", "123"], ["test", "123"]]，然后用requests实现登录接口的测试用例，断言http状态码，断言返回值。
'''

# 1. 账号信息
import requests     # 导入 requests 的包

aa = [["test", "123456"],["test","123456"]]


# 2.  取出每一次的账号


# 2.1  构造请求 
for a in aa:
    username = a[0]
    password = a[1]

    method  = "post"
    url ="http://132.232.44.158:5000/userLogin/"
    data = {"username":username,"password":password,"captcha":"123456"}

    
    res = requests.request(method = method,url=url,json=data)
    try:
        assert res.status_code ==200
        assert '"code": 200' in res.text
        print(" 测试用例执行通过！")
    except:
        print(" 测试用例执行失败！")
