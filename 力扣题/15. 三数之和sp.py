# @Time    : 2022/2/20 12:21
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 15. 三数之和sp.py
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    temp = [nums[i], nums[left], nums[right]]
                    if temp not in result:
                        result.append(temp)
                    left += 1
                    right -= 1
                elif sum > target:
                    right -= 1
                else:
                    left += 1
        return result
