# @Time    : 2022/2/22 23:58
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 5. 最长回文子串.py
class Solution:
    "以每个字母为回文中心,考虑回文长度为奇数和偶数的情况."
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.start = 0
        self.max_len = 0
        n = len(s)
        if n < 2:
            return s

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            if self.max_len < j - i - 1:
                # print(i,j)
                self.max_len = j - i - 1
                self.start = i + 1

        for k in range(n):
            #print(k)
            helper(k, k)
            helper(k, k + 1)
        return s[self.start:self.start + self.max_len ]