from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# 学习知识点
# find_element_by_name 寻找 name 属性， 即搜索框
# WebDriver 提供了许多寻找网页元素的方法，譬如 find_element_by_* 的方法
#  Keys 这个类来模拟键盘输入。

driver = webdriver.Chrome('/Library/Frameworks/Python.framework/Versions/3.6/chromedriver')
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")

elem.send_keys(Keys.RETURN)
print(driver.page_source)