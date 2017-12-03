import time


from selenium import webdriver
#firefox浏览器45版本以下不需要驱动的，45以上开始的firefox的浏览器也需要把driver。exe文件放到环境变量下边
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
#含蓄的委婉的
driver.implicitly_wait(30)
#driver.maximize_window()
driver.get("http://localhost/")
#点击登录按钮之前，我们要先删除target属性
#但是javascript定位比selenium麻烦
#可不可以用selenium的定位方式替换javascript的定位方式
#用arguments关键字，可以把元素定位作为一个参数替换，替换到javascript
login_link=driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("ctt")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("password").submit()
time.sleep(5)
#应该用隐式等待，自动判断网页是否加载完毕
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
iphone_img="body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img"
iphone_link2="body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a"
#img是标签名，表示前面的是父节点，后边是子节点
#想在.是class  nth表示第几个。表示父亲的第二个儿子
#css内容越短越好，涉及越多的网页元素，代码的可维护性就越差
#因为开发人员一旦修改页面时修改了这些节点，那么元素就会定位失败
iphone=driver.find_element_by_css_selector(iphone_link2)
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
#driver.find_element_by_class_name("goods-pay-btn-c goods-add").click()
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
driver.find_element_by_class_name("add-address").click()

driver.find_element_by_name("address[address_name]").send_keys("ctt")
driver.find_element_by_name("address[mobile]").send_keys("15890096743")
# driver.find_element_by_css_selector("[value='230000']").click()
# driver.find_element_by_css_selector("[value='230500']").click()
# driver.find_element_by_css_selector("[value='230506']").click()
sheng=driver.find_element_by_id("add-new-area-select")
Select(sheng).select_by_value("230000")

shi=driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_index(2)
xian=driver.find_elements_by_tag_name("select")[2]
Select(xian).select_by_visible_text("碾子山区")

driver.find_element_by_name("address[address]").send_keys("jinsong")
driver.find_element_by_name("address[zipcode]").send_keys("100010")

