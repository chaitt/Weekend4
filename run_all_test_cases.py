import unittest


if __name__ == '__main__':
    #defaultTestLoader默认的测试用例加载器，寻找符合规则的测试用例
    #discover 发现
    suite=unittest.defaultTestLoader.discover('./day5',pattern='*Test.py')
    #执行suite中的所有的测试用例,TextTestRunner文本测试用例运行器
    #TextTestRunner()首字母大写，说明是一个类，类不能直接调用方法
    #必须实例化之后才能调用
    #python中的实例化不需要new，直接在类后边加一个小括号就好
    unittest.TextTestRunner().run(suite)