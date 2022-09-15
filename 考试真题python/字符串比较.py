"""
给定字符串A、B和正整数V，A的长度与B的长度相等，请计算A中满足如下条件的最大连续字串的长度
１、该连续子串在A和B中的位置和长度均相同
２、该连续子串｜A［ｉ］－Ｂ［ｉ］｜之和小于等于V。其中｜A［ｉ］－Ｂ［ｉ］｜表示两个字母ASCII码之差的绝对值
输入描述
输入为三行：
第一行为字符串A，仅包含小写字符，1<=A.length<=10000
第二行为字符串B，仅包含小写字符，1<=B.length<=10000
第三行为正整数V，0<=V<=10000
输出描述：
字符串最大连续子串的长度，要求该子串｜A［ｉ］－Ｂ［ｉ］｜之和小于等于V
输入：
xxcdefg
cdefghi
5
输出
2
"""

import sys

string1 = sys.stdin.readline().strip("\n")
string2 = sys.stdin.readline().strip("\n")
V = int(sys.stdin.readline().strip("\n"))
sumlist = []
length = []
for i in range(len(string1)):
    sum1 = abs(ord(string1[i]) - ord(string2[i]))
    if sum1 < V:
        for j in range(i+1,len(string1)):
            sum1 = sum1+ abs(ord(string1[j]) - ord(string2[j]))
            if sum1 > V:
                break
            else:
               length.append(j-i+1)
    elif sum1 == V:
        length.append(1)
    else:
        length.append(0)
print(max(length))

