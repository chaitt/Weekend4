#2导入csv包
#csv是pathon语言内置的包，比较常用，开发和测试项目可能都用的到
import csv
#2存放路径
#字符前边加一个r，表示反斜杠是普通字符，不看做转义字符
path=r"C:\Users\51Testing\PycharmProjects\Weekend4\data\member_info.csv"
#3要想读取，首先通过路径打开文件
file=open(path,'r')
#4通过csv代码库，读取csv格式内容
data_table=csv.reader(file)
#遍历
for row in data_table:
    print(row)
