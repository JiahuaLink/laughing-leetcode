"""
输入一个英文字符串，要求非大小写英文字母均视为单词间隔符，输出单词逆序后的字符串，输出时单词间隔符仅以一个空格标志。例如“I am* a boy”，逆序排放后为“boy a am I”
"""

import re

str = input()
l1 = re.split('[^A-Za-z]', str)
l2 = list(reversed(l1))
while '' in l2:
    l2.remove('')
print(' '.join(l2))

"""
输入一个英文字符串，字符串中每个单词用空格隔开，句子中除了英文字母不再包含其他字符。输出单词逆序后的字符串。例如“I am a boy”，逆序排放后为“boy a am I”
"""
str = input()
strLi = list(reversed(str.split()))
print(' '.join(strLi))
