"""
输入两行字符串，第一行为需要加密的字符串，第二行为需要解密的字符串，按照加密解密规则输出两行，第一行为加密后的字符串，第二行为解密后的字符串。加密规则：将大写字母变换为该字母后一位字母、并小写输出，将小写字母变换为该字母后一位字母、并大写输出，将数字加1输出（9变换为0），其余字符不变。解密规则对应加密规则的逆过程。
"""

import re

alphaList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def Encrypt(aucPassword, aucResult=[]):
    for x in aucPassword:
        if re.match('[A-Z]', x):
            xLower = x.lower()
            idx = alphaList.index(xLower) + 1
            if idx == len(alphaList):
                idx = 0
            x = alphaList[idx]
        elif re.match('[a-z]', x):
            idx = alphaList.index(x) + 1
            if idx == len(alphaList):
                idx = 0
            x = alphaList[idx].upper()
        elif re.match('[0-9]', x):
            if x == '9':
                x = '0'
            else:
                x = str(int(x) + 1)
        aucResult.append(x)
    print("".join(aucResult))

def unEncrypt(password, result=[]):
    for x in password:
        if re.match('[A-Z]', x):
            xLower = x.lower()
            idx = alphaList.index(xLower) - 1
            if idx == -1:
                idx = len(alphaList)
            x = alphaList[idx]
        elif re.match('[a-z]', x):
            idx = alphaList.index(x) - 1
            if idx == -1:
                idx = len(alphaList)
            x = alphaList[idx].upper()
        elif re.match('[0-9]', x):
            if x == '0':
                x = '9'
            else:
                x = str(int(x) - 1)
        result.append(x)
    print(''.join(result))

pwdList = []
for i in range(2):
    pwdList.append(input())
Encrypt(pwdList[0])
unEncrypt(pwdList[1])
