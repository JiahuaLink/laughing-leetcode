# @Time    : 2021/11/13 1:00
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 有效的回文.py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''
        for i in s:
            if i.isalnum():
                ss += i
        ss = ss.lower()
        print(ss)
        i = 0
        j = len(ss) - 1
        while i < j:
            if ss[i] != ss[j]: return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = "race a car"
    print(Solution().isPalindrome(s))
