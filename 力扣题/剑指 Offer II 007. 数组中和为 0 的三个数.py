# @Time    : 2022/2/18 20:37
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 剑指 Offer II 007. 数组中和为 0 的三个数.py
# 思路：固定一个数字nums[i]，在nums[i+1]-nums[-1]之间采用双指针的方法，相当于确定两个数字之和为-nums[i]
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            target = 0 - nums[i]
            left = i + 1
            right = len(nums)-1
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


if __name__ == '__main__':
    nums = [0]
    print(Solution().threeSum(nums))
