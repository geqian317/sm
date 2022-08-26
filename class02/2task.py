
"""
    1.实现web端基于网易云音乐的QQ登录
    2.将网易云的元素定位都使用手写xpath完成
"""
from time import sleep

from selenium import webdriver


# 实例化对象
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
# 添加隐式等待
driver.implicitly_wait(10)
# 访问网易云音乐
driver.get('http://music.163.com')
# 最大化窗体 避免元素无法正常交互
driver.maximize_window()
print(driver.window_handles)
#sleep(2)
# 定位登陆元素,并点击
driver.find_element('xpath','//*[contains(@class,"s-")]').click()
#sleep(1)
# 选择其他方式登陆
driver.find_element('xpath','//a[contains(text(),"其他")]').click()
# 同意协议
driver.find_element('xpath','//input[@type="checkbox"]').click()
# 选择QQ登陆
driver.find_element('xpath','//*[contains(@class,"_3V")]').click()

print(driver.title)
# 获取当前页面的句柄
handles=driver.window_handles
# 关闭当前句柄
# driver.close()
# 切换句柄
# driver.switch_to.window(handles[1])
print(handles)

#sleep(2)

# 切换iframe: 通过下标
driver.switch_to.frame(0)
# 也可以直接传入id
# driver.switch_to.frame('ptlogin_iframe')
# 没有id通过元素定位
"""fr=driver.find_element('id','ptlogin_iframe')
driver.switch_to.frame(fr)"""
# 执行QQ快捷登陆
# 添加显示等待
"""el=WebDriverWait(driver,5,0.5).until(
    lambda el1:driver.find_element('xpath','//*[@id="img_out_330548527"]'),
    message='元素查找失败')
el.click()"""


# 返回,默认窗体
# driver.switch_to_default_content()
# driver.quit()


"""
    句柄: 1个标签页标识1个句柄
    通过selenium操作的标签页,在不切换的情况下,只会聚焦在第一个页面.
    需要的话通过driver.switch_to_handles[x]来切换句柄  x从0开始
    原则:
        1.在selenium自动化时,尽可能最多保留2个页面存在
        2.如果页面会自动关闭,就不需要额外执行close操作(特定业务)
        3.如果关闭后,仍需要操作其他页面,则需要切换句柄
"""


"""
    iframe: 是一个窗体,内嵌页面,是一个独立的HTML页面.类似于套娃
    遇到死活定位不到的元素,检查是否是iframe.如果是,切换iframe后操作
    iframe在切换进去之后,只能操作iframe里面的元素,如果要操作原窗体内容,需要重新返回默认窗体
"""

