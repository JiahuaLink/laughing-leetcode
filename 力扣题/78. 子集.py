# @Time    : 2022/2/18 21:00
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 78. 子集.py
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def to_do(start, tmp):
            result.append(tmp)
            for j in range(start, n):
                to_do(j + 1, tmp + [nums[j]])
        to_do(0, [])
        return result

nums = [1, 2, 3]
print(Solution().subsets(nums))
