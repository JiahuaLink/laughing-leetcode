# @Time    : 2021/11/13 0:33
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 左右两边子数组的和相等.py
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):

            # left = sum(nums[:i]) if nums[:i] else 0
            # right = sum(nums[i + 1:len(nums)]) if nums[i + 1:len(nums)] else 0
            # # print(left, right)
            if sum(nums[:i]) == sum(nums[i + 1:len(nums)]):
                return i

        return -1


if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    # print(nums[:6])
    print(Solution().pivotIndex(nums))
#
