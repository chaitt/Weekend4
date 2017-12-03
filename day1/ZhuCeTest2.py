#打开浏览器
from selenium import webdriver
driver =webdriver.Chrome()

#打开海盗商城主页
driver.get("http://localhost/")
#点击注册链接
#第四种元素定位方法：链接文本信息
driver.find_element_by_link_text("注册").click()
#输入用户信息
#切换窗口工作，selenium切换到新的窗口工作
cwh=driver.current_window_handle #浏览器当前窗口的句柄
#selenium只提供了工作的窗口的名字，并没有提供第二个窗口的名字
whs=driver.window_handles  #多个窗口的句柄
#for关键字 -集合中的某个元素 in关键字  数组/集合中的某个元素
#item表示whs元素中的一个元素，每次循环取一次值，循环结束
#whs中的每个元素都会被遍历一次
#遇到冒号下一行肯定要四个空格
for item in whs:
    if item == cwh:
        driver.close()  #关闭当前标签
    else:    #这种情况就是要找的窗口
        driver.switch_to.window(item)

driver.find_element_by_name("username").send_keys("changcheng")

#点击提交按钮
#登陆，把注册代码补全
