# 百度搜索
from time import sleep, time

from selenium import webdriver

# 创建一个webdriver对象
from selenium.webdriver.common.by import By

#driver=webdriver.Chrome()
# # 访问URL:一定要在URL中加//
#driver.get('http://www.baidu.com')
# # 输入'上林赋'
# # find_element_by_xpath被弃用,建议使用find_element(by.xpath,)的形式
# # driver.find_element_by_id('kw')
#driver.find_element('id','kw').send_keys('上林赋')
# # 点击百度一下
# driver.find_element('id','su').click()
# # 添加等待
# sleep(3)
# # 关闭浏览器,释放资源
# # quit是退出驱动,关闭所有 close是关闭当前窗口
# driver.quit()



# 底层源码解析 鼠标左键+Ctrl
from selenium.webdriver.chrome.webdriver import WebDriver

"""
从webdriver模块底层代码来了解selenium+webdriver对浏览器进行交互的全过程
"""
# Starts the service and then creates new instance of chrome driver.
# executable_path=DEFAULT_EXECUTEABLE_PATH 如果没有安装在默认路径下,在这里更换路径
# 创建一个webdriver对象
wd=WebDriver(executable_path='chromedriver')
# 访问URL
#  get=self.execute(Command.GET, {'url': url})
wd.execute('get',{'url':'http://www.baidu.com'})
# 查找元素
# 通过name查找,如果找到返回一个对象, 没有找到抛出异常
# self.execute(Command.FIND_ELEMENTS, {
#             'using': by,      和comment一样封装了一个类
#             'value': value})['value'] or []
# 运行后报错
'''el=wd.execute('findElement',{
     'using':'id',
     'value':'kw'})['value']'''
el=wd.execute('findElement',{
    'using':'xpath',
    'value':'//input[@id="kw"]'})['value']
#print(type(el))
el._execute('sendKeysToElement',{
    'text':'上林赋',
    'value':''})
# 定位百度一下
el=wd.execute('findElement',{
    'using':'xpath',
    'value':'//input[@id="su"]'})['value']
el._execute('clickElement')
sleep(3)
wd.quit()
