#打开浏览器
from selenium import webdriver
#从selenium 导入 网络驱动（平时用的鼠标，代码模拟需要用网络驱动），用来操作浏览器的
driver=webdriver.Chrome()
#给打开的网络驱动起的名字叫driver,运行可以打开浏览器的驱动
#python语言不需要加分号
#第二个chrome后边一定要有括号
#第三个字体的问题file-settings--editor---color and font

#打开登陆页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#输入用户名,寻找用户名的输入框   网页上所有可见的都属于element，link，按钮，下拉框
#在叫driver的浏览器上寻找网页元素，如果id等于‘username’那么向页面元素中发送键盘上长城这几个按键
driver.find_element_by_id("username").send_keys("ctt")
#输入密码
driver.find_element_by_id("password").send_keys("123456")
#点击登陆按钮
#如果我们使用一个方法，这个方法没有提示信息，就不存在
driver.find_element_by_class_name("login_btn").click()



