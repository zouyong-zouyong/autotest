# # unittest 的测试用例

# #  先导入unittest
# import time
# import unittest 
# from selenium import webdriver   # 导入selenium

# # 1.测试用例必须要继承的 unittest.TestCase)
# class TestCaseLogin(unittest.TestCase):

#     # 2.成员方法名字以 test_
#     def test_01_login_success(self):
#         chromedriver ='driver\\chromedriver.exe'
#         driver = webdriver.Chrome(executable_path=chromedriver)  # 实例化浏览器（打开浏览器，获得操作对象）
#         driver.maximize_window()   # 浏览器变成全屏
#         driver.get("http://132.232.44.158:9999/shopxo/admin.php")  # 打开网址

#         # 去查找用户名密码、登录
#         #  方法1 ：Xpath方法
#         # driver.find_element_by_xpat('/html/body/div[1]/div/div[2]/div/form/div/div[1]/input').send_keys('admin')
#         # driver.find_element_by_xpat('/html/body/div[1]/div/div[2]/div/form/div/div[2]/input').send_keys('shopxo')
#         # driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()
        

#         #方法2 ：name方法 或 id方法
       
#         driver.find_element_by_name('username').send_keys('admin')
#         driver.find_element_by_name('login_pwd').send_keys('shopxo')
#         driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()
   

#         #断言 ——unittest断言
#         time.sleep(5)
#         url = driver.current_url  # 获取网址
#         self.assertEqual(url,"http://132.232.44.158:9999/shopxo/admin.php?s=/index/index.html")
#         print("01")

#     def test_02_login_failed(self):  
#         print("02")



# # unittest 自带的运行方法，不用实例化类的方法
# # unittest.main()  

#=========================================================================


# unittest 的测试用例

#  先导入unittest
# import time
import unittest 
from selenium import webdriver   # 导入selenium

# 1.测试用例必须要继承的 unittest.TestCase)
class TestCaseLogin(unittest.TestCase):

    # 2.成员方法名字以 test_
    def test_01_login_success(self):
        chromedriver = 'E:\\PYPro\\ZYpython\\unittesttes\\driver\\chromedriver.exe'
        driver = webdriver.Chrome(executable_path=chromedriver)  #实例化浏览器，  打开浏览器
        driver.maximize_window()
        driver.get("http://132.232.44.158:9999/shopxo/admin.php")  # 打开网址


    def test_02_login_failed(self):  
        print("登陆失败")
 
# unittest 自带的运行方法，不用实例化类的方法 
unittest.main()  

        # chromedriver ='driver\\chromedriver.exe'
        # driver = webdriver.Chrome(executable_path=chromedriver)  # 实例化浏览器（打开浏览器，获得操作对象）
        # driver.maximize_window()   # 浏览器变成全屏



