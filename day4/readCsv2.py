#1之前的readcsv不能被其他测试用例调用，所以应该给这段代码封装到一个方法
#2每个测试用例的路径不同，所以path应该作为参数传入到这个方法中
#4我们打开了一个文件，但是并没有关闭，最终会造成内存泄露
import csv
import os


def read(file_name):
    #所有的重复代码的出现都是程序设计有问题
    #重复的代码应该单独封装到一个方法里
    current_file_path =os.path.dirname(__file__)
    path=current_file_path.replace("day4","data/"+file_name)
    #file=open(path,'r')
    #with语句是一个代码块，代码块中的内容都要缩进四个空格
    #with代码块可以自动关闭with中声明的变量file
    result=[]
    with open(path,'r')as file:
        data_table=csv.reader(file)
        for row in data_table:
            result.append(row)
    return result

    #如果在打开程序和关闭程序的代码之间发生了异常情况，导致后边的代码不能正常执行
    #file.close()也不能执行，这时文件仍然不能关闭
    #应该用with_as实现文件的关闭
    file.close()
if __name__ == '__main__':
    #path = r"C:\Users\51Testing\PycharmProjects\Weekend4\data\member_info.csv"
    #read(path)
    # 3.这个路径是一个绝对路径，我们工作中一个项目不仅一个人编写代码
    # 没法同意要求大家都把项目代码放在一个文件夹下边
    # 这个文件因为在项目中，它的路径也会随着项目变化
    # 所以应该在代码中自动的找到相对路径，通过当前代码文件的路径，根据相对位置找到csv文件
    # 首先要找到当前文件路径
    #os是操作系统，path是路径，dir是directory
    #__file__是python内置的变量，指的是的当前的文件
    # current_file_path =os.path.dirname(__file__)
    # path=current_file_path.replace("day4","data/member_info.csv")
    # print(current_file_path)
    # 我们真正想要的路径是csv文件的路径member_info.csv
    #print(path)
    member_info=read("member_info.csv")
    for row in member_info:
        print(row[0])
    print(member_info)



