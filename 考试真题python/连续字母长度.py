"""
给定一个字符串，只包含大写字母，求再包含同一个字母的子串中，长度第K长的子串的长度，相同字母只取最长的那个子串
输入：
AAAAHHHBBCDHHHH
3
输出：
2
"""

import sys
string1 = sys.stdin.readline().strip("\n")
K = int(sys.stdin.readline().strip("\n"))
string2 = set(string1)
countlist = []
for i in string2:
    countlist.append(string1.count(i))
countlist.sort(reverse=True)
print(countlist[K-1])
