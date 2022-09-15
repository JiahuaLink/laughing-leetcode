# @Time    : 2022/2/20 18:44
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 77. 组合.py
'''回溯
                1. 不剪枝：436ms
                2. 剪枝：36ms！！
                原理:   1. 组合剩余需要元素个数：k-len(path)
                        2. 设nums = [1,2,3,4,5,6], k = 4, 此时len(path) = 2
                        3. 还需要2个元素，i至少从5即下标4开始遍历
                            i的右边界 = n - (k-len(path)) = 6-2=4
                        则i的for循环范围就是(start, n-(k-len(path))+1)
                '''
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        start = 1

        def dfs(n, k, start):
            for i in range(start, n - (k - len(path)) + 2):
                if len(path) == k:
                    res.append(path[:])
                    return
                path.append(i)
                dfs(n, k, i + 1)
                path.pop()

        dfs(n, k, start)
        return res


n, k = 4, 2
print(Solution().combine(n, k))
