# @Time    : 2021/11/13 1:12
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 最多删除一个字符得到回文.py
class Solution:
    def validPalindrome(self, string: str) -> bool:
        s = list(string)
        i = 0
        j = len(s) - 1
        if Solution().isPalindrome(''.join(s)):
            return True
        while i < j:

            if s[i] != s[j]:
                tempa = s.pop(i)

                if Solution().isPalindrome(''.join(tempa)):

                    return True
                tempb = s.pop(j)
                if Solution().isPalindrome(''.join(tempb)):
                    # print(kk, j)
                    return True
                print(s)
            i += 1
            j -= 1
        return False

    def isPalindrome(self, ss: str) -> bool:

        i = 0
        j = len(ss) - 1
        while i < j:
            if ss[i] != ss[j]: return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = "aaaabcaaaa"
    print(Solution().validPalindrome(s))

    # s = ['a','b','c']
    # s.pop(1)
    # print(''.join(s))
