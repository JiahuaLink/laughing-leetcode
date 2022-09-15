# @Time    : 2021/11/26 0:33
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 213. 打家劫舍 II.py
"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

"""思路核心原则就是：第一个和最后一个不能同时抢。 所以：要么不抢第一个，要么不抢最后一个。 注意，不抢第一个的时候，最后一个可抢可不抢；另一种情况同理 取两种情况中的最大值"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return
        if len(nums) == 1:
            return nums[0]

        # 初始化两个方案
        state1 = [0] * len(nums)
        state2 = [0] * len(nums)

        # 方案1 是不抢第一个房屋，那么算法就是state1[0] =0 来计算（最后一个可抢可不抢）
        for i in range(0, len(nums)):
            if i == 0:
                state1[0] = 0  # 因为不抢了 那就为0
            elif i == 1:
                state1[1] = max(state1[0], nums[1])
            else:
                state1[i] = max(state1[i - 2] + nums[i], state1[i - 1])

        # 方案2 是不抢最后一个房屋(遍历不到最后一个房子)，那么算法就是state1[0] =num[0] 来计算（第一个可抢可不抢,直接取值）
        for i in range(0, len(nums) - 1):
            if i == 0:
                state2[0] = nums[0]  # 第一个可抢可不抢,直接取值
            elif i == 1:
                state2[1] = max(state2[0], nums[1])
            else:
                state2[i] = max(state2[i - 2] + nums[i], state2[i - 1])
        return max(state1[len(nums) - 1], state2[len(nums) - 2])


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
