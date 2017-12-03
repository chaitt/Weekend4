import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage
from day6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
        #打开网页
        #self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
        lp=LoginPage(self.driver)
        lp.open()
        lp.input_username("ctt")
        lp.input_password("123456")
        lp.click_login_button()
        pcp=PersonalCenterPage(self.driver)
        time.sleep(5)
        self.assertEqual(pcp.title,self.driver.title)
        # #输入用户名
        # self.driver.find_element(By.ID,"username").send_keys("ctt")
        # #输入密码
        # self.driver.find_element(By.ID, "password").send_keys("123456")
        # #点击登陆按钮
        # self.driver.find_element(By.CLASS_NAME,"login_btn").click()
        # #验证是否跳转管理中心页面
        # expected="我的会员中心 - 道e坊商城 - Powered by Haidao"
        # time.sleep(5)
        # self.assertIn("我的会员中心",self.driver.title)

