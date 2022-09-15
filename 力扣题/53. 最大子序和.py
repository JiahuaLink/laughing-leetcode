# @Time    : 2021/11/20 1:11
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 53. 最大子序和.py
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        sum = 0
        for i in nums:
            # 假设sum<=0，那么后面的子序列肯定不包含目前的子序列，所以令sum = num；如果sum > 0对于后面的子序列是有好处的。res = Math.max(res, sum)保证可以找到最大的子序和。
            if sum > 0:
                # 遇到正数就贪婪去取
                sum += i
            else:
                # 遇到负数的情况下  是不利的  就重新给sum赋值
                sum = i
            res = max(res, sum)
        return res


if __name__ == '__main__':
    nums = [1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
