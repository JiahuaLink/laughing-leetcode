# @Time    : 2021/12/21 0:20
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 46. 全排列.py
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        global count
        count = 0

        def dfs(path: list, choice):
            global count
            if len(path) == len(nums):
                count += 1
                result.append(path[:])
                return
            for item in choice:
                if item in path:
                    continue
                path.append(item)
                dfs(path, choice)
                path.pop()

        dfs([], nums)
        return result


print(Solution().permute([1, 2, 3]))
