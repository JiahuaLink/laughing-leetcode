"""
输入两个数组和一个数k，数组1和数组2中的数组成一对数，求k对数的最小和，每个数组的长度不超过100
例：
输入
array1：3 1 1 2
array2：3 1 2 3
k:2
输出
4
"""
import heapq


array1 = input().split()
array2 = input().split()
k = int(input())
if len(array1) >= 100 or len(array2) >= 100:
    print("字符串长度超过标准")
else:
    size1 = min(int(array1[0]),len(array1)-1)
    size2 = min(int(array2[0]),len(array2)-1)
    array3 = []
    for i in range(1,size1+1):
        for j in range(1,size2+1):
             heapq.heappush(array3,[int(array1[i]),int(array2[j])])
    min = 0
    for i in range(k):
        min += sum(array3[i])
    print(min)




