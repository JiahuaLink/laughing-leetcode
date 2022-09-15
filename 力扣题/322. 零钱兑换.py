# @Time    : 2022/2/22 20:27
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 322. 零钱兑换.py
'''
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
题目求的值为 f(11)，第一次选择硬币时我们有三种选择。

假设我们取面额为 1 的硬币，那么接下来需要凑齐的总金额变为 11 - 1 = 10，即 f(11) = f(10) + 1，这里的 +1 就是我们取出的面额为 1 的硬币。

同理，如果取面额为 2 或面额为 5 的硬币可以得到：

f(11) = f(9) + 1
f(11) = f(6) + 1
所以：

f(11) = min(f(10), f(9), f(6)) + 1
'''
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''版本一'''
        # 初始化
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        # 遍历物品
        for coin in coins:
            # 遍历背包
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1
coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))