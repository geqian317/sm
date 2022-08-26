"""
    1. 实现电商系统的用户注册与登录流程的自动化测试
    账号密码请自行添加
    商城url：http://39.98.138.157/shopxo/index.php
"""
from time import sleep

from selenium import webdriver

# 创建webdriver对象
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(10)
# 访问商城
driver.get('http://39.98.138.157/shopxo/index.php')
# 窗体最大化
driver.maximize_window()
# 定位注册并点击
driver.find_element('xpath','//a[text()="注册"]').click()
# 定位到用户名,点击并输入
un=driver.find_element('xpath','//input[@name="accounts"]')
un.click()
un.send_keys('gq_1990')
# 定位到密码,点击并输入
pwd=driver.find_element('xpath','//input[@name="pwd"]')
pwd.click()
pwd.send_keys('123456')
# 勾选协议
driver.find_element('xpath','//*[@class="am-icon-checked"]').click()
# 点击注册
driver.find_element('xpath','//form[contains(@class,"username")]/div[4]/button').click()
# 通过显示等待判断是否注册过:
in_sign=WebDriverWait(driver,5,0.5).until(
    lambda el:driver.find_element('xpath','//*[contains(text(),"已存在")]')
    ,message='元素定位失败')
exit=driver.find_element('xpath','//*[contains(@class,"am-close")]')

# 定位到退出按钮,并点击退出
login_suc=WebDriverWait(driver,5,0.5).until(
    lambda el:driver.find_element('xpath','//a[text()="退出"]')
    ,message='元素定位失败')
print('登陆成功')
login_suc.click()


# 登陆
driver.find_element('xpath',"//div[@class='member-login']/a[1]").click()
# 定位用户名,点击,输入
un1=driver.find_element('xpath','//input[@name="accounts"]')
un1.click()
un1.send_keys('gq_1990')
# 定位密码,点击,输入
pwd1=driver.find_element('xpath','//input[@name="pwd"]')
pwd1.click()
pwd1.send_keys("123456")
# 电机的登陆
driver.find_element('xpath','//*[contains(@class,"btn-lo")]').click()


