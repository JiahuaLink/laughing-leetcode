"""
幼儿园两个班的小朋友在排队时混在了一起，每位小朋友都知道自己是否与前面一位小朋友是否同班，请你帮忙把同班同学找出来
小朋友的编号为整数，与前一位小朋友同班用Y表示，不同班用N表示
输入：
１/N　２/Y　３/N ４/Y  5/N
输出　
编号按照大小升序排序，分班记录中第一个编号小的排在第一行
若只有一个班的小朋友，第二行为空行
若输入不合符要求，则直接输出字符串ＥＲＲＯＲ
１２
３４　
"""

import sys
array1 = sys.stdin.readline().strip("\n").split()
result = []
array2 = []
if "Y" in array1[0]:
    print("ERROR")
else:
    for i in range(len(array1)):
        if "Y" in array1[i]:
            array2.append(array1[i - 1].split("/")[0])
            array2.append(array1[i].split("/")[0])
        if len(array2) != 0 and "N" in array1[i] or  i == len(array1) -1:
            result.append(list(set(array2)))
            array2 = []
if len(result) > 1:
    for i in result:
        i.sort(key=lambda x:int(x))
        print("".join(i))
else:
    result[0].sort(key=lambda x: int(x))
    print("".join(result[0]))
    print("\n")
