"""
要求：1s 262144k
给定一个随机的整数数组（含正负整数），找出其中的两个数，其和的绝对值为最小值，并返回两个数，按从小到大返回以及绝对值。每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍

输入：通过空格分割的有序整数序列字符串，最多1000个，范围（-65535，65535）
输出：两数之和的绝对值最小值

eg:
输入： -1 -3 7 5 11 15
输出：-3 5 2

"""
# !/usr/bin/python
# -*- coding: utf-8 -*-
nums = sorted(input().split(" "))
sum_dict = {}
minsum = -1
for x in range(0, len(nums) - 1):
    for y in range(x + 1, len(nums)):
        sum = abs(int(nums[x]) + int(nums[y]))
        if minsum == -1 or sum < minsum:
            minsum = sum
            numx = nums[x]
            numy = nums[y]
            if numx > numy:
                t = numx
                numx = numy
                numy = t
print(numx, numy, minsum)
