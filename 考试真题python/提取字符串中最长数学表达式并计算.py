"""
提取字符串中的最长合法简单数学表达式，字符串长度最长的，并计算表达式的值。如果没有返回0.
简单数学表达式只能包含以下内容：
0-9数字，符号+=*
说明：
1.所有数字，计算结果都补偿过Long
2.如果有多个和长度一样的，请返回第一个表达式的结果
3.数学表达式，必须是最长的合法的
4.操作符不能连续出现，如±-+1是不合法的
输入描述：
字符串
输出描述：
表达式值
示例：
输入：
1-2abcd
输出
-1
"""

import  re  ##re模块为高级字符串处理提供了正则表达式工具
inputStr=input()
line =re.findall("[-+*0-9]+",inputStr)
for item in line:
    num = 0
    for i in range(len(item)-1):
        if  ("-" or "+" or"*") in item[i] :
            if("-" or "+" or"*") in item[i+1] : ##判断操作符连续
                  num += 1
    if num > 1:
        line.remove(item)
# print(line)
for item in line:
    lens = 0
    for i in range(len(item)-1):#判断是否有连续的运算符
        if item[i] in ["-","+","*"] and item[i+1] in ["-","+","*"]:
            lens += 1
    if lens > 0:
        line.remove(item)
# print(line)
res = sorted(line, key=lambda x:len(x),reverse=True)##按表达式长度排序
if len(res) <= 0:
    print("0")
else:
    t=res[0]
    n = 0
    count = 0
    for i in range(len(t)):
        if t[i] in ["-", "+", "*"]:
            n += 1
        elif t[i].isdigit():
            count +=1
    if n >= 1 and n + 1 == count:
        print(eval(t))
    else:
        print("0")
