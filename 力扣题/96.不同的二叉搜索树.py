# @Time    : 2022/2/19 15:43
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 96.不同的二叉搜索树.py
class Solution:
    def numTrees(self, n: int) -> int:
        dp = (n + 1) * [0]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


print(Solution().numTrees(3))
