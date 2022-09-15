"""
游戏规则：输入一个只包含英文字母的字符串，字符串中的两个字母如果相邻且相同，就可以消除。
在字符串上反复执行消除的动作，知道无法继续消除为止，此时游戏结束。
输出最终得到的字符串的长度。
输入描述：
输入原始字符串str，只能包含大小写英文字母，字母的大小写敏感，str长度不超过100
输出描述：
输出游戏结束后，最终得到的字符串长度。
备注：
输入中包含非大小写英文字母时，均为一场输入，直接返回0
示例：
输入：
gg
输出：
0
"""
inputStr = input()
line = []
for item in inputStr:
    if len(line) == 0:
        line.append(item)
    elif item == line[-1]:
        line.pop()
    else:
        line.append(item)
if inputStr.isalpha():
    print(len(line))
else:
    print(0)
