"""
要求：1s 262144k
公司用一个字符串来表示员工的出勤信息：
absent 缺勤
late 迟到
leaveearly 早退
present 正常上班
能获得全勤奖的条件：
缺勤次数不超过1次
不能连续迟到/早退
任意的连续7次考勤中，缺勤、迟到、早退的次数不超过3次
eg:
输入：
2
present
present present
输出：true true
输入：
2
present
leaveearly late present present
输出： true false
"""

import sys


def award(s):
    if s.count('absent') > 1:  ##判断缺勤不超过1次
        return 'false'
    if s.count('late late') > 0 or s.count('leaveearly leaveearly') > 0 or s.count('late leaveearly') or s.count(
            'leaveearly late'):  ##判断没有连续的迟到早退
        return 'false'
    sl = s.split(" ")  ##把每行字符串转换成列表
    for i in range(len(sl)):  ##判断任意连续7次考勤，迟到早退和缺勤不超过3次
        if sl[i] == 'absent' or sl[i] == 'late' or sl[i] == 'leaveearly':
            num = 0
            l = sl[i + 1:i + 7]
            num += l.count('absent')
            num += l.count('late')
            num += l.count('leaveearly')
            if num > 2:
                return 'false'
    return 'true'


n = int(sys.stdin.readline())  ##标准输入
res = []
for i in range(n):
    line = sys.stdin.readline().strip()  ##strip()以换行分割
    res.append(award(line))
print(" ".join(res))
