"""
    三类等待
    1.强制等待
        sleep() 时间以秒为单位 在time包下的类
        不考虑代码整体的连贯性,遇到强制等待时,等待到指定时间.时间结束后,在运行后面的代码
        优势: 容易上手,也可以方便调试代码
        劣势: 迟钝,在自动化执行时会造成大量时间浪费
    2.隐式等待
        时间以秒为单位,一般而言等待的时间设置为5s或者10s
        是driver的一个设置项,只需要设置一次,在driver的整个周期中生效
        找到元素后停止等待,若没有找到元素,等待时间结束后,会继续运行后面的代码
        隐式等待必须要等待页面加载完成后,再生效,所以效率提升不是很明显.
        但是我们关注的不是页面是否加载完成,我们更关注某个元素是否加载完成.
        优势: 设置一次,存在与driver的整个生命周期(一般而言,隐式等待都会添加)
        劣势: 找不到元素就不找了
    3.显式等待
        专门针对元素来设置的等待
        调用时需要定义
        分为until和until_not两个函数来实现等待,意义相反
        若找到元素,return元素; 若未查找到,抛出timeout异常
        优势: 针对单个元素进行等待,效率高(也可以当做断言)
        劣势: 代码过长,用起来麻烦
    实际的自动化测试中:三类等待是综合应用的.
        当显式等待和隐式等待共同存在时:
        1.如果显式等待的元素查找失败, 会抛出超时异常
        (因为隐式等待没有异常, 除非是定位元素定位错误而报错)
        2.基于两者等待时间的设置, 默认遵循时间最长的等待
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
# 隐式等待
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
driver.find_element('xpath','//*[@id="kw"]').send_keys('上林赋')
driver.find_element('xpath','//*[@id="su"]').click()

# 显式等待  等待哪个浏览器,等待时间,等待频率
WebDriverWait(driver, 5, 0.5).until(
    lambda el:driver.find_element('xpath','//a[contains(text(),"赋作")]')
    ,message='元素查找失败')
driver.find_element('xpath','//a[contains(text(),"赋作")]').click()
# 查找正确后的打印
print('这是查找之后的')

# 定位元素成功,return 返回查找的元素
"""el=WebDriverWait(driver, 5 ,0.5).until(
    lambda el1:driver.find_element('xpath','//a[contains(text(),"赋作")]')
    ,message='元素查找失败')
# 可以通过找到的元素去定位元素,去点击,去输入
el.click()"""


# until_not  查找元素等待元素消失,元素消失后等待结束
"""el=WebDriverWait(driver,5,0.5).until_not(
    lambda el1:driver.find_element('xpath','//a[contains(text(),"赋作")]')
    ,message='元素查找失败')
el.click()"""
# 因为元素未消失,查找失败,所以超时异常


"""
    弹窗机制:
        现阶段大多数的弹窗交互都是基于div层直接实现的
        有的弹窗不是页面弹出的,而是浏览器弹出的
        浏览器弹窗,有三种形式:
        alert:确认     prompt:输入并确认    confirm:确认与取消
      若弹窗样式与操作系统一个风格,则一定是alter
      若弹窗样式与软件系统一个风格,一般是div,只需要考虑是否存在iframe即可  
"""
# 切换到弹窗
alert=driver.switch_to.alert
# alert弹窗处理
alert.accept()
# prompt弹窗处理
alert.accept()
alert.dismiss()
alert.send_keys()
# confirm弹窗处理
alert.accept()
alert.dismiss()
# 获取alert弹窗的文本
text=alert.text





