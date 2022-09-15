"""
输入两个数组和一个数K，数组1和数组2中的数会组成一对数，求K对数的最小和，每个数组的长度不超过100
输入：
Array1:3 1 1 2
Array2:3 1 2 3
K:2
输出：4
说明：
两个数组的第一个数为数组长度（即array1的第一个数3是计算需要用到的数组[1,1,2]的长度，数组长度不超过100，从第一个数组和第二个数组中各取一个数进行组合成一对数，求k对数的最小和
示例中array1和array2可以组成的对数有{[1,1],[1,2],[1,3],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3]},需要取其中K对数计算最小的和
其中[1,1]和[1,1]的和最小，为1+1+1+1=4,输出4

"""

import sys

array1 = sys.stdin.readline().strip("\n").split()
array2 = sys.stdin.readline().strip("\n").split()
k = int(sys.stdin.readline().strip("\n"))

size1 = min(int(array1[0]), len(array1) - 1)
size2 = min(int(array2[0]), len(array2) - 1)
array3 = []
for i in range(1, size1 + 1):
    for j in range(1, size2 + 1):
        array3.append([int(array1[i]), int(array2[j])])
array3.sort(key=lambda x: x[0] + x[1], reverse=False)
minsum = 0
for i in range(k):
    minsum += sum(array3[i])
print(minsum)
