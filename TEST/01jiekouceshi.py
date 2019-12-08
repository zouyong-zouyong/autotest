# 导入 requests 
import requests 



url = "http://www.weather.com.cn/data/sk/101010100.html"      # 定义url变量存放网址
res = requests.get(url)                                      # 请求get方法请求网址，把获得的结果，保存在res变量中
a = res.text
# print(a)


# 取返回值里面 time的值
b = res.json()        # 把返回值转换成字典
# print(b)

time = b["weatherinfo"]["time"]   #取出time值
print(time)










