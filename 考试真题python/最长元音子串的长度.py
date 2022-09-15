"""
当一个字符串只有元音字母（aeiouAEIOU）组成，称为元音字符串。现给定一个字符串，找出其中最长的元音字串子串，并返回其长度；如果找不到，则返回0。
子串：字符串中任意个连续的字符组成的子序列称为该字符串的子串。

输入描述：一个字符串，其长度范围[0,65535],字符串仅由字符a-z和A-Z组成
输出描述：一个整数，表示最长的元音字符串子串的长度。
"""

inputStr = input()
vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
for i in inputStr:
    if  i not in vowels:
        inputStr = inputStr.replace(i,'0')
# print(inputStr)
line = inputStr.split("0")
# print(max(line))
print(len(max(line)))
