"""
不使用内置方法，将字符串数字转为int数字。
例：
输入：“123”
输出：123
"""

# -*- coding:utf-8 -*-

s = input()
s1 = s[::-1]
num = 0
for i,v in enumerate(s1):
    for j in range(10):
        if v == str(j):
            num = num + j * (10**i)
print(num)
