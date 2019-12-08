# 如何编写selenium的jiaobu


# 第一步：导入selenium的第三方包
from selenium import webdriver


# 第二步： 打开谷歌浏览器

driver = webdriver.Chrome(executable_path=".\chromedriver.exe")
# 第三步： 打开百度
driver.get("https://www.baidu.com/")

# 第四步：输入搜索关键字
element1 = driver.find_element_by_id("kw")
element1.send_keys("hello seleninm!")


# 第五步：点击搜索按钮
element2 = driver.find_element_by_id("su")
element2.click()



# # 最后一步：结束测试
# driver.quit()