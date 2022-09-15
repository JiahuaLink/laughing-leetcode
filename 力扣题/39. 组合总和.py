# @Time    : 2022/2/20 11:39
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 39. 组合总和.py
# @Time    : 2022/2/20 0:32
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 90. 子集 II.py
import copy
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start, candidates, path, res, target):
            if target == 0:
                res.append(copy.deepcopy(path))
                return

            for i in range(start,len(candidates)):
                if candidates[i] <= target:
                    path.append(candidates[i])
                    dfs(i, candidates, path, res, target - candidates[i])
                    path.pop()

        dfs(0, candidates, path, res, target)
        return res

candidates,target = [2,3,6,7], 7
print(Solution().combinationSum(candidates,target))