"""
输入n+1行，第一行为一个正整数n(1≤n),下面n行为n个整数，构成一个整形数组（可能有正数和负数），求该数组中连续子数组（最少有一个元素）的最大和。要求时间复杂度为O(n)。
"""


# -*- coding:utf-8 -*-

def getMax(a, b):
    if a > b:
        return a
    else:
        return b


num = int(input())
a = []
for i in range(num):
    a.append(int(input()))
sum = a[0]
max = a[0]
for i in a[1:]:
    sum = getMax(sum + i, i)
    max = getMax(sum, max)
print(max)
