# @Time    : 2021/11/25 23:56
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 198. 打家劫舍.py
from typing import List


class Solution:
    """
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def rob(self, nums: List[int]) -> int:
        # 设置状态方程
        if not nums: return
        if len(nums) == 1:
            return nums[0]
        state = [0] * len(nums)
        # 如果只有一个房间，直接取该房间的金额

        # 如果有两间房，只能取一个  那就只能取最大的那一个的方案

        # 如果有3间房，那就是取当前房子的值+第一个（i-2）的总和，和前面只有两间房子的方案state[1]的最大值比较
        # state[3] = max(nums[2], state[2])
        for i in range(0, len(nums)):
            if i == 0:
                state[0] = nums[0]
            elif i == 1:
                state[1] = max(state[0], nums[1])
            else:
                state[i] = max(state[i - 1], state[i - 2] + nums[i])
        return state[len(nums) - 1]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))
