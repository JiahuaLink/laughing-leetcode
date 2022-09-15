"""
【正序和最小】
给定一个正序数组，包含正数、负数和0，找出其中任意两个数，输出最小和的绝对值
例：
输入 -3 -1 5 7 9
输出 2

"""

import sys

numlist = sys.stdin.readline().strip("\n").split()
result = []
for i in range(len(numlist)):
    for j in range(i+1,(len(numlist))):
        sumNum = int(numlist[i])+int(numlist[j])
        result.append(abs(sumNum))
print(min(result))