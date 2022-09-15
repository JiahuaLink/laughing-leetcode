# @Time    : 2022/1/24 23:22
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 计算某字母出现次数.py
# 写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字母，然后输出输入字符串中该字母的出现次数。不区分大小写。
#
# 输入描述:
# 第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字母。
#
# 输出描述:
# 输出输入字符串中含有该字符的个数。



def find_nums_instr():
    count=0
    ss = input().strip()
    key = input().strip()
    for i in ss:
        if i.lower() == key.lower():
            count+=1
    print(count)
find_nums_instr()
