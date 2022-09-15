# @Time    : 2022/2/19 20:51
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 34. 在排序数组中查找元素的第一个和最后一个位置.py
# 利用二分思想先找其左边界，再找其右边界即可，注意找左边界的时候，由右侧逼近；找右边界的时候，由左侧逼近，即可。
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        res = list()
        # 计算左边界
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        # 不存在，直接返回
        if nums[l] != target:
            return [-1, -1]
        res.append(l)
        # 计算右边界
        i = l
        while i < len(nums) and nums[i] == target:
            i += 1
        res.append(i - 1)
        return res


nums, target = [5, 7, 7, 8, 8, 10], 8
print(Solution().searchRange(nums, target))
