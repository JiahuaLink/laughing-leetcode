"""
输入一行或多行字符串密码，验证每行密码是否符合规范，符合提示“OK”，否则“NG”。密码规范为：
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度超2的子串重复
"""

import sys
import re

def has_Dup(str):
    for i in range(len(str)-3):
        for j in range(i+1, len(str)-3):
            if str[i:i+3] == str[j:j+3]:
                return True

def check_pwd(pwd):
    if len(pwd) <= 8 or has_Dup(pwd):
        return False
    count = 0
    if re.search('[0-9]', pwd):
        count += 1
    if re.search('[a-z]', pwd):
        count += 1
    if re.search('[A-Z]', pwd):
        count += 1
    if re.search('\W', pwd):
        count += 1
    if count >= 3:
        return True


pwdList = sys.stdin.readlines()
for x in pwdList:
    x = x.strip()
    if check_pwd(x):
        print('OK')
    else:
        print('NG')
