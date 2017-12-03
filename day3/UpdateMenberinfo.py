#登陆
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("ctt")
#链表和数组不同，数组有固定的长度，链表必须有明确的结尾标志
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
#对着整个浏览器输入
#点击进入账号设置
driver.find_element_by_link_text("账号设置").click()
#点击个人资料
driver.find_element_by_partial_link_text("个人资料").click()
#修改个人信息
#clear清空的意思，用来清楚元素中原本的内容
#每次执行sendkeya之前都进行一遍clear操作
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("真实姓名")
#性别
#css可以用多个属性组合定位一个元素
#一个元素的多个属性之间不能有空格
driver.find_element_by_css_selector("#xb[value='2']").click()
#和pathon语法不一样
# js='document.getElementById("date").removeAttribute("readonly")'
# driver.execute_script("js")
# driver.find_element_by_id("date").clear()
# driver.find_element_by_id("date").send_keys("2006-11-21")

#用arguments改写上边的输入：用selenium定位，定位之后用javascript删掉
#
date1=driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")',date1)
date1.clear()
date1.send_keys("1980-11-21")

# 1.用selenium调用javascript一共有两个关键字：1，arguments[0]表示用python语言代替一部分javascript
#好处是有时selenium定位比较容易
#2，return把javascript的执行结果返回给python语言
#好处是，有时selenium定位不到的元素可以用javascript定位到


# date=driver.execute_script("return document.getElementById('date')")
# date.click()

driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("74211359")
driver.find_element_by_class_name("btn4").click()

#右键检查不了html代码的弹出框叫做arert，有单独的方法来处理
time.sleep(3)
#alert控件不是html代码生成的，所以上边写了implicitly_wait，这个time.sleep（）方法不能用
#切换到alert的方法，和切换窗口的方法类似
#alert弹出框，accept接受，同意，确定，dissmiss拒绝取消
driver.switch_to.alert.accept()



















