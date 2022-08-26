"""
    八大元素定位法则（开发者工具中，Elements标签页下，通过Ctrl+F显示元素查找框）
    1.id：基于标签的id属性进行定位，类似身份证，基本不会重复，提前校验避免重复
    2.name：类似姓名，容易重名
    3.link text：用于定位超链接（a标签），通过a标签的文本进行定位
    4.partial link text：用于定位a标签，通过模糊查找的形式来实现定位，类似于MySQL中的like关键字
        一般partial定位会出现多元素的结果，可以通过find elements来进行定位
        (1)不加s的定位，默认返回查找到的第一个结果
        (2)加s的定位，基于下标的选择来返回元素
    5.tagname：基于标签名定位，一般不推荐，只有在特殊情况下使用（表格：多个商品）
    6.classname：极其不推荐,除非实在没有办法
    7.cssselector：定位界的万金油之一, #表示id(只在这里) 专治IE浏览器下元素定位的疑难杂症,可以通过copy复制
        伪元素：有些特定数据是在调用页面的时候,通过接口通信生成的,一般常见于下拉列表框.通过cssselector定位
        例如  ::before::
             ::after::
             通过QQ截屏识图(Ctrl+Alt+O):  div.wrap.f-cb
    8.xpath：万金油，基于树状结构来进行定位的，类似于文件机制
        (1)绝对路径：/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input
            不建议使用绝对路径，因为页面会经常维护，而且数标签容易出错
        (2)相对路径：通过语法来实现元素的定位
        //input[@id='su']   从根路径下查找id为su的input标签
        //*[text()='新闻']
          //     从根路径下开始查找，从HTML标签开始
          input  查找的元素标签名称  * 表示查找全部标签
          []     添加筛选条件，多条件用and进行关联
          @      Attribute 属性
          text()   固定写法，专属通过text文本来查找元素的筛选条件.text内容需完全符合一致
        //input[@type='hidden and @name='ch']
        (3)xpath中元素定位的方法很多,经常用到的就是相对路径，和爸爸找儿子.
            爸爸找儿子  //form[@name='f']/input[5]
            儿子找爸爸  //input[@type='hidden']/..
            儿子找兄弟  //input[@type='hidden']/.
        在查找元素时推荐自上而下的进行查找(从上的话使用相对路径,//form[@name='f']/input[5])
        (3)xpath中常用的函数
            contains：通过模糊查找的行为查找元素.可以通过属性,文本作为查找条件
            //input[contains(@id,'kw')]
            //a[contains(text(),'新')]
            //i[contains(@class,'k')]

"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
# 1.通过name定位
#el=driver.find_element('name','wd')
#print(type(el))


# 2.通过id定位
#el=driver.find_element('id','su')
#print(type(el))


# 3.通过link text进行'新闻'的定位
#el=driver.find_element('link text','新闻')
#el.click()


# 4.通过partial link text进行'国'的定位(百度热搜中的超链接)
#el=driver.find_element('partial link text','国')
#el.click()
# 添加等待时间,不然页面没有加载完,会报错
#sleep(10)
#el=driver.find_element('partial link text','百度')
# 默认返回第一个搜索到的内容
#print(el.text)
# elements的定位返回的是一个list,所有符合条件的元素全部放在一个list中,就算只有1个元素
#els=driver.find_elements('partial link text','百度')
#for el in els:
#    print(el.text)


# 5.通过tagname进行元素定位（都是基于复数的s进行定位）
#els=driver.find_elements('tag name','a')
#for el in els:
#    print(el.text)


# 6.通过classname定位,通过标签class属性定位,不推荐 class中的属性太多了
#driver.find_element('class name','bg s_btn')


# 7.通过cssselector定位元素
# '#'表示id
#driver.find_element('css selector','#kw').send_keys('上林赋')
#driver.find_element('css selector','#su').click()
#sleep(3)
#driver.quit()
# 伪元素
"""driver.get('http://music.163.com')
sleep(2)
el=driver.find_element('css selector','div.wrap.f-cb')
print(el)"""


# 8.通过xpath定位
# 通过By筛选器实现8种不同的元素定位
# driver.find_elements(By.XPATH,'//*[contains(text(),"新")]')  #返回1个列表
# driver.find_element('xpath','//a[contains(text(),"新")]')    # 返回第一个
# By.XPATH=='xpath'
# 本质是一样的，都是字符串。区别是By需要导包
