import time
from selenium import webdriver
#firefox浏览器45版本以下不需要驱动的，45以上开始的firefox的浏览器也需要把driver。exe文件放到环境变量下边
driver=webdriver.Chrome()
#含蓄的委婉的
driver.implicitly_wait(30)
#窗口最大化
driver.maximize_window()
driver.get("http://localhost/")
#点击登录按钮之前，我们要先删除target属性
#但是javascript定位比selenium麻烦
#可不可以用selenium的定位方式替换javascript的定位方式
#用arguments关键字，可以把元素定位作为一个参数替换，替换到javascript
login_link=driver.find_element_by_link_text("登录")
driver.execute_script("argument[0],removeAribute('target')",login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("ctt")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("password").submit()
#submit用于提交
time.sleep(5)
#应该用隐式等待，自动判断网页是否加载完毕

driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
iphone_img="body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"
driver.find_element_by_css_selector(iphone_img).send_keys("")













