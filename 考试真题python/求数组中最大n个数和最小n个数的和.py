"""
输入一个数 M ，表示数组中有 M 个数。输入 M 个数。输入 n，求数组 M 中，去除重复值后，最大 n 个数和最小 n 个数的和
注意：最大和最小的数中不能有重复值，否则输出 -1
样例输入
5
3 3 2 4 2
2
样例输出
-1
说明
去除重复后最大的2个数为[4,3]，最小的2个数为[2,3]；有相同值，所以返回-1
样例输入
5
3 3 2 4 2
1
样例输出
6
说明
去除重复后最大的1个数为[4]，最小的1个数为[2]；没有相同值，返回6
"""

import sys
M = int(sys.stdin.readline().strip("\n"))
numlist = list(set(sys.stdin.readline().strip("\n").split(" ")))
n = int(sys.stdin.readline().strip("\n"))
numlist.sort()
length = min(len(numlist),M)
if length / 2 >= n:
    result = 0
    for i in range(n):
        result += int(numlist[i])+int(numlist[length-1-i])
else:
    result = -1
print(result)