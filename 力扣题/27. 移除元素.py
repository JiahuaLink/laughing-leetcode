# @Time    : 2021/12/16 23:11
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 27. 移除元素.py
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        i = 0

        while i <= j:
            if nums[j] == val:
               nums.remove(nums[j])

            j -= 1
        return nums

if __name__ == '__main__':
    nums = [3]
    print(Solution().removeElement(nums, 3))
