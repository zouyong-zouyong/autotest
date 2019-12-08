# 异常处理ZL：处理代码报错的情况
# 代码报错时， 终端会输出错的原因

a = [1,2,3,4,5,6,]

try:
    a[4]
    print(a,"没有报错")
except:
    print("内容报错")

#     for循环 
# list ,知道循环次数有限的时候
for a in [1,2,3,4,5,6]:
    print(a)

    
i = 0
# 不断的去执行代码的时候
while i<10:
    i =i+1
    print(i)


print("...........................")



from selenium import webdriver
driver = webdriver.Chrome(executable_path="Chromedriver.exe")


driver.get("http://132.232.44.158:9999/shopxo/index.php")
