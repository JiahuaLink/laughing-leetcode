"""
【字符串消消乐】
题目：给定一个字符串，从左往右扫描，如存在两个或两个以上的相同字符靠在一起，则消除这些字符。对每次消除后剩下的字符，继续应用上述规则，直到不能再消除为止。
分析：
"""

class Solution:
    def removeLetter(self,letterstr):
        s = []
        del_str = ''
        for letter in letterstr:
            if len(s) == 0:
                s.append(letter)
                del_str = ''
            else:
                if letter == del_str:
                    continue
                elif letter == s[-1]:
                    del_str = s.pop(-1)
                else:
                    s.append(letter)
                    del_str = ''
        return "".join(s)


p = Solution()
print(p.removeLetter('abcccbxezzzrf7788fn'))

