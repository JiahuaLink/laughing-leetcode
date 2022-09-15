"""
将密码按照规则从明文转变为密文，输入为密码明文，密码长度不超过100个字符、不包含空格，需要输出相应密文。转变规则：明文中大写字母转变为小写字母并后移一位，
明文中小写字母按照手机9键键盘进行转变（abc–2, def–3, ghi–4, jkl–5, mno–6, pqrs–7, tuv–8 wxyz–9），数字和其他的符号都不做变换。

"""

import re

alphaList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str1 = input()

output = []
for x in str1:
    if re.match('[A-Z]', x):
        xLower = x.lower()
        idx = alphaList.index(xLower) + 1
        if idx == len(alphaList):
            idx = 0
        x = alphaList[idx]
    elif re.match('[a-z]', x):
        if x in 'abc':
            x = '2'
        elif x in 'def':
            x = '3'
        elif x in 'ghi':
            x = '4'
        elif x in 'jkl':
            x = '5'
        elif x in 'mno':
            x = '6'
        elif x in 'pqrs':
            x = '7'
        elif x in 'tuv':
            x = '8'
        elif x in 'wxzy':
            x = '9'
    output.append(x)
print(''.join(output))
