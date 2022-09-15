"""
磁盘的容量单位常用的有M，G，T这三个等级，关系为 1T = 1024G、1G = 1024M，如样例所示先输入磁盘的个数，再依次输入磁盘的容量大小，然后按照从小到大的顺序对磁盘容量进行排序并输出。
样例：
输入：
3
1G
2G
1024
输出：(容量相等，保留原来的相对位置)
1G
1024
2G

"""

import sys
n = int(input())
line = []
for i in range(n):
    line.append(sys.stdin.readline().strip())
res = []
for item in line:
    if item[-1] == 'M':
        item2 = str(int(item[:-1])*1024)
    elif item[-1] == 'G':
        item2 = str(int(item[:-1])*1024*1024)
    elif item[-1] == 'T':
        item2 = str(int(item[:-1])*1024*1024*1024)
    else:
        item2 = item
    res.append((item,item2))

def sorted_by_count(x):
    return x[1]
sortRes = sorted(res, key=sorted_by_count)
for i in sortRes:
    print(i[0])
