"""
连续输入2次字符串，并按长度为8拆分每个字符串，然后输出到新的字符串数组，拆分规则是：若字符串不是8整倍数需要右侧补数字0，空字符串不处理。

做题思路
思路一：输入的字符串长度不足8位或者不是8的整数倍，都右补0，补齐后的新字符串满足为8的整数倍，然后将新字符串按照下标进行每8位分隔至一个list中
思路二：输入的字符串长度不足8位或者不是8的整数倍，都右补0，补齐后的新字符串满足为8的整数倍，然后用re.findall(’.{8}, 补齐后的str)
"""
import math

def cut_8ch(str):
    if len(str) < 8:
        str = str.ljust(8, '0')
    elif len(str) > 8:
        if (len(str) % 8) != 0:
            width = math.ceil(len(str) // 8) * 8
            str = str.ljust(width, '0')
    str2List = []
    i = 0
    while i < len(str):
        if (i + 8) < len(str):
            str2List.append(str[i:i+8])
        else:
            str2List.append(str[i:len(str)])
            break
        i = i + 8
    return str2List

output = []
for i in range(2):
    tmp = input().strip()
    output.append(cut_8ch(tmp))

for x in output:
    for y in x:
        print(y)
