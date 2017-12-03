from selenium.webdriver.common.by import By


class LoginPage:
    #构造方法的作用
    #实例化登陆对象的时候，需要把driver作为参数传进来,实例化对象的时候必须要调用构造方法
    # #python中构造方法是固定的写法 ，__init__初始化
    #方便别的属性或者方法使用driver
    def __init__(self,driver):
        self.driver=driver

    title="用户登录 - 道e坊商城 - Powered by Haidao"
    url="http://localhost/index.php?m=user&c=public&a=login"

    #小括号是元祖，元祖中的两个值，第一个元素是控件的定位方式
    #第二个元素是网页控件的具体的值
    username_input_loc=(By.ID,"username")
    password_input_loc=(By.ID,"password")
    login_button_loc=(By.CLASS_NAME, "login_btn")



    def open(self):
        self.driver.get(self.url)

    def input_username(self,username):
        #self.driver.find_element_by_id("username").send_keys(username)
        #星号的作用把一个元祖中的元素分别传入方法参数中
        #前边的一个星号，表示传入的就不是元祖了，而是元祖中的两个元素
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()


