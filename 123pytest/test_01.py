# 首先导入pytest
import pytest
import requests

# 定义 pytest 的测试用例
def test_01_login_success():
    url ="http://132.232.44.158:5000/userLogin/"
    data =  {"username":"test", "password":"123456", "captcha":"123456"}
    res = requests.post(url=url,json=data)
    print(res.text)

    # 断言HTTP状态码
    assert 200== res.status_code
    assert '"code": 200' in res.text
    
    


