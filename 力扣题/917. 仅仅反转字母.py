# @Time    : 2022/2/23 22:51
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 917. 仅仅反转字母.py
import re


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = re.findall('[A-Za-z]', s)

        n = len(s)
        result = n*['0']
        for i in range(n):
            if s[i].isalpha():
                result[i] =letters.pop()
            else:
                result[i] = s[i]
        return ''.join(result)

s = "Test1ng-Leet=code-Q!"

print(Solution().reverseOnlyLetters(s))
