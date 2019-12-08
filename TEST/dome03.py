# 二次封装   (实现代码的复用，方便下次用)

# 自己写的 search_butth 方法
def find_element(driver,search_buttn):
    from selenium.webdriver.support.ui import WebDriverWait
    return WebDriverWait(driver,10).until(lambda s: s.find_element(*search_buttn))