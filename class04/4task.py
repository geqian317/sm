'''
    通过自动化测试行为，实现电商的下单流程。
    登录-搜索商品-添加商品属性-加入购物车-校验购物车是否添加成功
    推荐使用商品是手机，iPhone 6
'''
from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://39.98.138.157/shopxo/index.php')
driver.find_element('xpath','//div[@class="menu-hd"]/a[1]').click()
driver.find_element('xpath','//form[contains(@class,"user")]/div[1]/input').send_keys('gq_1990')

driver.find_element('xpath','//form[contains(@class,"user")]/div[2]/div/input')