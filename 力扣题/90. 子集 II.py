# @Time    : 2022/2/20 0:32
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 90. 子集 II.py
import copy
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def backtrack(nums, startIndex):
            if copy.deepcopy(path) not in res:
                res.append(copy.deepcopy(path))
            #
            # res.append(path[:])
            for i in range(startIndex, len(nums)):
                # 我们要对同一树层使用过的元素进行跳过
                if i < startIndex and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(nums, i + 1)
                path.pop()
        # 去重需要排序
        nums.sort()
        backtrack(nums, 0)
        return res



nums = [1,2,2]
print(Solution().subsetsWithDup(nums))