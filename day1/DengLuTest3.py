#javascript  是一门独立的语言
#1元素定位 ：id----name---class
#link_test必须是链接，必须是<a>标签，必须是文本
#2元素的操作：鼠标左键单机click，发送键盘上的按键send_keys
#3学好javascript

#用javascript实现窗口切换
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost/")
#在python中执行javascript
js='document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)
#点击登陆链接
driver.find_element_by_link_text("登录").click()
#输入用户名密码
driver.find_element_by_id("username").send_keys("ctt")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_class_name("login_btn").click()


