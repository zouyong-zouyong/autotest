#     作业
'''
1. 作业，使用selenium编写自动化测试脚本
    要求：首先登录后台 （admin /shopxo)
              点击用户管理 - 用户列表 - 新增
              新增用户之后，去判断用户名是不是和输入的一致。
              ("a" in "abc")
'''

# # 1.如何编写selenium脚本
# import time    # 导入运行time ，不那么快
# from selenium.webdriver.support.ui import WebDriverWait

# from selenium import webdriver    #  第一步：调入第三方包
# driver = webdriver.Chrome(executable_path="chromedriver.exe")   # 第二步：打开谷歌浏览器
# driver.maximize_window()   #第三步：窗口最大化
# # 第四步： 进入ShopXo的后台管理员服务
# driver.get("http://132.232.44.158:9999/shopxo/admin.php?s=/admin/logininfo.html")  

# # 第五步：定位元素 （输入登账号）
# e = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/form/div/div[1]/input")
# e.send_keys("admin")

# #第六步（输入密码）
# e = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/form/div/div[2]/input")
# e.send_keys("shopxo")

# # 第七步 点击登录
# time.sleep(5)   #    降低速度 5 秒
# denglu = '/html/body/div[1]/div/div[2]/div/form/div/div[3]/button'
# dl = driver.find_element_by_xpath(denglu)
# dl.click()

# #第八步：点击用户管理
# time.sleep(3)   #    降低速度 3 秒
# djyhgl = '//*[@id="admin-offcanvas"]/div/ul/li[5]/a/span[2]'
# yhgl = driver.find_element_by_xpath(djyhgl)
# yhgl.click()


# #第九步：点击用户列表
# time.sleep(2)
# yh = driver.find_element_by_id("power-menu-126")
# yh.click()





import time

from selenium import webdriver        # 导入 selenium 的三方包
driver = webdriver.Chrome(executable_path="chromedriver.exe") # 打开谷歌浏览器
driver.get("http://132.232.44.158:9999/shopxo/admin.php?s=/admin/logininfo.html")   #进入网址



#  在同一页面的情况下，可以这么操作
# 先找 元素
u = driver.find_element_by_name("username")        
p = driver.find_element_by_name("login_pwd")
dl = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/form/div/div[3]/button")

#  然后来再来 操作，输入用 】‘户名和 密码
u.send_keys("admin")
p.send_keys("shopxo")
dl.click()


# 点击户户管理---用户列表
time.sleep(6)
yhgl = driver.find_element_by_xpath('//*[@id="admin-offcanvas"]/div/ul/li[5]/a')  #点击用户管理
yhgl.click()
time.sleep(3)
yhlb = driver.find_element_by_xpath('//*[@id="power-menu-126"]/li/a')       #  点击用户列表
yhlb.click()

# 切换作用域
xzbb = driver.find_element_by_id('ifcontent')
driver.switch_to_frame(xzbb)

#  新增 按钮
xz = driver.find_element_by_xpath('/html/body/div[1]/div/div/a[1]')
xz.click()

time.sleep(3)
# 输入用户信息，增加用户
yhm =driver.find_element_by_name('username')
dlmmm = driver.find_element_by_name('pwd')
djdl = driver.find_element_by_xpath('/html/body/div[1]/div/form/div[14]/button')


mz = "海贼王"
yhm.send_keys(mz)
dlmmm.send_keys("123456")
djdl.click()

time.sleep(3)

##data-list-393 > td.user-info > ul > li:nth-child(1)
#  获取名字 和 输入的值 进行 对比
a = driver.find_element_by_xpath('//*[@id="data-list-394"]/td[2]/ul/li[1]')
if mz in a.text:
    print("执行通过")
else:
    print("执行失败")







