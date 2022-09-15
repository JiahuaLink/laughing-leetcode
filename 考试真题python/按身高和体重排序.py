"""
某学习举行运动会，学生们按编号（1，2，3…n）进行标识，嫌需要按照身高由低到高排序；对身高相同的人，按体重由轻到重排列；对于身高体重都相同的人，维持原有的编号顺序关系。请输出排列后的学生编号。

输入描述：
两个序列，每个序列由n个正整数组成（0<n<100）。第一个序列中的数值代表身高，第二个序列中的数值代表体重。
输出描述：
排列结果，每个数值都是原始序列中的学生编号，编号从1开始

示例：
4
100 100 120 130
40 30 60 50
输出：2 1 3 4

示例：
3
90 110 90
45 60 45
输出：1 3 2
"""
n = int(input())
height = input().split()
weight = input().split()

arr1 = []
for i in range(n):
    arr1.append(((int(height[i]), int(weight[i])), i + 1))


def sorted_by_length_weight(x):
    return x[0][0], x[0][1]


arr2 = sorted(arr1, key=sorted_by_length_weight)
print(" ".join(str(x) for x in list(tuple(i[1] for i in arr2))))
