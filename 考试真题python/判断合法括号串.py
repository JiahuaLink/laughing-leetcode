"""
给定一个字符串A，请设计一个算法，判断其是否为一个合法的括号串。若合法返回True，否则返回False
例：
输入(()())
返回：True
输入：()a()()
返回：False
"""
# -*- coding:utf-8 -*-

def chkParenthesis(self, A):
    stackA = []
    for i in A:
        if i == '(':
            stackA.append(i)
        elif i == ')':
            if not stackA:
                return False
            else:
                stackA.pop()
        else:
            return False
    return True

str = input()
print(chkParenthesis(str))
