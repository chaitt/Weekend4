from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.implicitly_wait(30)
#登陆
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_name("userverify").submit()
#商品管理
driver.find_element_by_link_text("商品管理").click()
#添加商品
driver.find_element_by_link_text("添加商品").click()

driver.switch_to.frame("mainFrame")
#商品名称
driver.find_element_by_name("name").send_keys("iphone")
#商品分类
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
#双击是特殊的元素的操作，被封装到ActionChains这个类中
#java封装到Actions这个类中
#链表结束必须以perform结尾
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()


driver.find_element_by_css_selector("[value='1']").click()
driver.find_element_by_class_name("button_search").click()




#商品品牌
#点击提交
