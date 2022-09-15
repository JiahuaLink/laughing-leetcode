"""
给定一个时间点，时间点中的所有数字可以重复使用，要求输出离给定时间点最近的下一个时间点
例：
输入 18：53
输出 18:55
输入：23：59
输出：22：22(下一天)
22:39
23:22
09:59
"""

import sys

array1 = sys.stdin.readline().strip("\n").replace(":", "")
arraylist = [int(i) for i in array1]
numlsit = sorted(list(set(arraylist)))
if max(numlsit) > arraylist[3]:
    index = numlsit.index(arraylist[3])
    arraylist[3] = numlsit[index+1]
else:
    arraylist[3] = numlsit[0]
    index = numlsit.index(arraylist[2])
    if numlsit[index + 1] < 6:
        arraylist[2] = numlsit[index + 1]
    else:
        arraylist[2] = numlsit[0]
        if arraylist[0] == 2:
            index = numlsit.index(arraylist[1])
            if numlsit[index + 1] >= 4 and arraylist[0] != 2:
                arraylist[1] = numlsit[index + 1]
            else:
                arraylist[1] = numlsit[0]
        else:
            if max(numlsit) > arraylist[1]:
                index = numlsit.index(arraylist[1])
                arraylist[1] = numlsit[index + 1]
            else:
                arraylist[1] = numlsit[0]

print(str(arraylist[0]) + str(arraylist[1]) + ":" + str(arraylist[2]) + str(arraylist[3]))