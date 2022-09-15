"""
描述
对于一个字符串，请设计一个高效算法，计算其中最长回文子串的长度。

给定字符串A以及它的长度n，请返回最长回文子串的长度。

示例1
输入：
"abc1234321ab",12
复制
返回值：7
"""

class Solution:
    def getLongestPalindrome(self, A, n):
        # write code here
        assert len(A) == n
        max_L = 1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if A[i:j + 1] == A[i:j + 1][::-1]:
                    L = j - i + 1
                    if L > max_L:
                        max_L = L
        return max_L

p = Solution()
print(p.getLongestPalindrome("abc1234321ab",12))