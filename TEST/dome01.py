# ===========================基础，都要 必 须 要 掌 握 ====================

# 1.如何编写selenium脚本
import time    # 导入运行time ，不那么快

#导入selenium的第三方包
from selenium import webdriver

#  打开谷歌浏览器,实例化浏览器。driver 称为浏览器操作的句柄
driver = webdriver.Chrome(executable_path="chromedriver.exe")
#  Chrome 是 谷歌浏览器。    executable_path= 是 可执行通过

driver.maximize_window()   # 窗口最大化

# 打开网站的网址： http://132.232.44.158:9999/shopxo/index.php
driver.get("http://132.232.44.158:9999/shopxo/index.php")

#定位元素
# 1. id 值
e =driver.find_element_by_id("search-input")
e.send_keys("华为")  #  在元素中输入 关键字

anniu =driver.find_element_by_id("ai-topsearch")
anniu.click()      # 点击 元素

# #  2。name
# e1 =driver.find_element_by_name("ai-topsearch")
# el = click()

#  1. sleep   
#  获取价格
time.sleep(3)   #    降低速度 3 秒
jiage = "/html/body/div[4]/div/ul/li/div/p[2]/strong"
jg = driver.find_element_by_xpath(jiage)
print(jg.text)    #运行文件格式

# 点击图片
time.sleep(3)   #    降低速度 3 秒
tupian ='/html/body/div[4]/div/ul/li/div/a'  # 里面有可能是 双引号，所以图片这里写 单引 （ 外双内单，外单内双）
tp = driver.find_element_by_xpath(tupian)
tp.click()      # 点击图片


#  切换 window 的作用
#  固定的代码 
w1 = driver.window_handles[-1]    #最后一个窗口： -1：表示list的最后一个元素
driver.switch_to_window(w1)   # 把driver 的作用域切换到最后一个窗口了，driver就可以重新跳转出来的窗口操作了


gm = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[3]/div[2]/div/button")
gm.click()


#  切换大网页和小网页的作用
f = driver.find_element_by_xpath('//*[@id="common-popup-modal-login"]/div/iframe')
driver.switch_to_frame(f)

#去输入：username
u = driver.find_element_by_name("accounts")
u.send_keys("123546789")

#  退出
# driver.quit()


