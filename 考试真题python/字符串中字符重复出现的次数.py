"""
输入两个字符串，两个字符串由数字、字符和空格组成，求出字符串1中出现的所有字符出现在字符串2中的综总次数，不区分大小写，字符串长度小于1000、
例：
输入
array1：”A ABbcH3gr12 “
array2：”abc“
输出
5
"""

array1 = input().lower()
array2 = input().lower()
if len(array1) >= 1000 or  len(array2) >= 1000:
    print("字符串长度超过标准")
else:
    times = 0
    for i in array1:
        for j in array2:
            if i == j:
                times += 1
    print(times)

