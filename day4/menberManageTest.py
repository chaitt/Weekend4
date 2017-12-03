import unittest
#导入ddt代码库
import ddt

import time
from selenium import webdriver

from day4.readCsv2 import read

#2装饰这个类
@ddt.ddt
class MemberManageTest(unittest.TestCase):
    #3调用之前写好的read（）方法，获取配置文件中的数据
    member_info=read("member_info.csv")
    global driver

    @classmethod
    def setUpClass(cls):
        print("所有方法之前执行一次")
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        #cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        #cls.driver.quit()

    def test_a_log_in(self):
        print("登陆测试")
        drver=self.driver
        self.driver.get("http://localhost/admin.php")
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("userpass").send_keys("password")
        self.driver.find_element_by_name("userverify").send_keys("1234")
        self.driver.find_element_by_name("userverify").submit()
    #python中集合前边的星号的表示，表示把集合中的所有的元素拆开，一个一个的写
    #list=["小红","小明"]
    #星号的作用就是把一个列表拆成两个string
    #加入一个方法接受两个参数，那么肯定不能传一个list进去
    #但是如果list中正好两个元素，这时的列表的前边加一个星号
    #这时就不认为这是一个list而是两个参数了
    #$ddt.data,测试数据来源于read（）方法中了
    #把数据的每一行传入方法，在方法里边增加一个参数row
    @ddt.data(*member_info)
    def test_b_add_menber(self,row):
        #每组测试数据就是一条测试用例，每条测试用例都是独立的，不能因为上一条的失败导致下一条不能用
        #不推荐for循环
        #应该用ddt装饰器，去修饰这个方法，达到每条测试用例独立执行的目的
        #ddr数据驱动测试
        #注释掉所有的for循环
        #for row in read("member_info.csv"):
            #print("添加会员")
        driver = self.driver

        self.driver.find_element_by_link_text("会员管理").click()
        self.driver.find_element_by_link_text("添加会员").click()
        #如果frame没有name属性，我们可以通过其他方式定位iframe标签，把定位好的元素传过去
        iframe_css="#mainFrame"
        iframe_html=driver.find_element_by_css_selector(iframe_css)
        self.driver.switch_to.frame(iframe_html)
        self.driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.find_element_by_css_selector('[value="{0}"]'.format(row[2])).click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()

        #之前代码能够运行，但是还不能自动判断程序是否正确
        #actual实际结果，执行测试用例之后页面上实际显示的结果
        actual=driver.find_element_by_css_selector("##datagrid-row-r1-2-0 > td:nth-child(1) > div")
        #expected期望结果，手动测试用例，需求文档，配置文件
        excepted=row[0]
        #断言类似于if。。else语句是用来做判断的
        if actual==excepted:
            print("测试通过")
        else:
            print("测试失败")

        #断言叫做assert，断言是框架提供的，要想调用断言加上self.因为测试用例的类继承了框架中的TestCase类
        #也继承了这个类中的断言
        #断言有几个特点：
        #1断言比较简洁
        #2断言只关注于错误的测试用例，
        #3只有断言出错的时候才会打印信息，正确没有任何信息
        #4断言报错的时候后边的代码将不会继续执行
        #





        #切换到父框架
        #driver.switch_to.parent_frame()
        #切换到网页的根节点
        driver.switch_to.default_content()
        self.assertEqual(actual, excepted)

if __name__ == '__main__':
    unittest.main()



