# 定位元素

# 导入appium的Python第三方包
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '5.1.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'vivo x6plus d'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'io.appium.android.apis'       # app的名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['appActivity'] = '.ApiDemos'                   # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘                # 设置成appium自带的键盘


    # 去打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 定位app按钮

# accessibility id
app = driver.find_element_by_accessibility_id("App")
app.click()


# Xpath
# app1 = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="App"]')
# app1.click()


# resourceid
# acc = driver.find_element_by_id('android:id/text1')
# acc.click()

# 文不值
# aaa = driver.find_element_by_android_uiautomator('new UiSelector().text("content")')
# aaa.click()


app2 = driver.find_element_by_accessibility_id("Search")
app2.click()

app3 = driver.find_element_by_accessibility_id("Invoke Search")
app3.click()

app4 = driver.find_element_by_id("io.appium.android.apis:id/txt_query_prefill")
app4.click()

