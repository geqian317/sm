# 只有input标签才可以实现sendkeys(), 文本域 textarea貌似也可以(不常见)
# 账号和密码的输入也是sendkeys(),因为也是input标签
# input的文件上传也可以用sendkeys(), 不是input标签的文件上传,用autoIT
# driver.find_element('xpath', '//*[@id="stfile"]').send_keys(r'D:\头像\1.jpg')
from selenium import webdriver
from selenium.webdriver.support.select import Select



"""
    下拉列表框: 
    当前的一般都是基于div或者input来实现的.样式是下拉列表框,但本质上不是下拉列表框
      1.div下拉列表框: 通过2次点击来获取你要的值
      2.input下拉列表框:
        可以通过2次点击来获取值(最稳妥的方式)
        也可以通过修改readonly的属性,再sendkeys输入值
    传统的下拉列表框: select标签,下方是option
        1.定位select元素
        2.转成select对象
        3.基于下标、value、text三种方式来获取元素    
"""
#创建对象
driver=webdriver.Chrome()
# 访问URL
driver.get('http://www.baidu.com')
# 定位 上传图片按钮
driver.find_element('xpath','//*[@class="soutu-btn"]').click()
img=driver.find_element('xpath','//input[@class="upload-pic"]')
#img.click()  不需要点击,直接通过send_keys上传
img.send_keys(r'C:\Users\Thomas\Desktop\wx.png')



# 定位select元素
"""el=driver.find_element('name','schoolid')
# 转成select对象
select=Select(el)
# 获取options的多有内容
li=select.options
for i in li:
    print(i)
# 基于下标 默认选择算,从0开始
select.select_by_index(1)
# 基于value
select.select_by_value('2913')
# 基于text
select.select_by_visible_text('北京八中固安分校')
"""
