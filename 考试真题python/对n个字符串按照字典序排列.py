"""
输入n+1行，第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。需要将n个字符串按照字典排序输出。

解题思路
1.读取输入正整数num
2.再循环读取num行字符串，并放入列表中
3.循环比较列表中的元素，第一次比较将最小元素与第一个元素位置调换，第二次比较将第二小元素与第二个元素位置调换
"""


def swap(a, b):
    tmp = a
    a = b
    b = tmp


n = input()
strs = []
for i in range(int(n)):
    str = input()
    strs.append(str)

num = int(n)
for k in range(num):
    min = strs[k]
    min_idx = k
    for i in range(k + 1, num):
        if strs[i] < min:
            min = strs[i]
            min_idx = i
    print(min)

    tmp = strs[k]
    strs[k] = min
    strs[min_idx] = tmp
