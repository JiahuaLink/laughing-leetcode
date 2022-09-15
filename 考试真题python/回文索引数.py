"""
输入N+1行，第一行为整数N（大于等于1），表示测试数据的组数，后面N行仅由小写字母组成的字符串。现在请找出一个位置，删掉那个字母之后，字符串变成回文。请放心总会有一个合法的解。如果给定的字符串已经是一个回文串，那么输出-1
"""
# -*- coding:utf-8 -*-

def isPalindrome(str):
    str1 = str[::-1]
    if str == str1:
        return True
    else:
        return False

def str_remove(str, idx):
    tmpList = list(str)
    tmpList.pop(idx)
    return "".join(tmpList)

num = int(input())
a = []
for i in range(num):
    a.append(input())

for x in a:
    if isPalindrome(x):
        print("-1")
    else:
        for i in range(len(x)):
            xNew = str_remove(x, i)
            if isPalindrome(xNew):
                print(i)
                break
            else:
                continue
