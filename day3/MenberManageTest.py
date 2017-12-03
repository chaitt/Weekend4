import unittest

import time
from selenium import webdriver


class MemberTest(unittest.TestCase):
    #变量前边加上self.表示这个变量是类的属性，可以被所有的方法访问
    def setUp(self):
        self.driver=webdriver.Chrome()
        #打开浏览器
        #driver声明在setup方法之内，不能被其他方法访问
        self.driver.implicitly_wait(30)
        #driver.maximize_window()
    def tearDown(self):
        #quit()退出整个浏览器
        #close()关闭一个浏览器标签
        #代码编写和调试的时候需要在quit方法前加一个时间等待方便看清楚执行的过程
        #正式运行的时候去掉时间等待，为了提高程序执行的速度
        time.sleep(20)
        #self.driver.quit()

    def test_add_member(self):
        driver=self.driver  #成员变量改变成局部变量
        driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("userpass").send_keys("password")
        driver.find_element_by_name("userverify").send_keys("1234")
        driver.find_element_by_name("userverify").submit()
        driver.find_element_by_link_text("会员管理").click()
        # driver.find_element_by_link_text("添加会员").click()
        # driver.find_element_by_name("username").send_keys("abc")
        # driver.find_element_by_name("mobile_phone").send_keys("15512345678")







