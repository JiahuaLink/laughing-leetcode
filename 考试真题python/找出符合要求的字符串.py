"""
要求：1s 262144k
给定两个字符串，从字符串2中找出字符串1的所有字符，并去重后按ASCII排序
"""

# !/usr/bin/python
# -*- coding: utf-8 -*-
s1, s2 = input().split()  ##将输入分割成两个字符串
res = set([])  ##set去重
for i in s1:
    if i in s2:
        res.add(i)  ##res类型为集合
print("".join((lambda x: (x.sort(), x)[1])(list(res))))
## x为形参，（x.sort(),x）为返回值,或者写成：
## print(" ".join(sorted(list(res))))
