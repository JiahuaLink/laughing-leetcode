"""

"""

# coding:utf-8;
"""思路：将输入的字符写入list中，然后使用sort（）函数进行排序，然后输出"""
n = int(input())
s = []
for i in range(n):
    s.append(input())
s.sort()
print('\n'.join(s))
