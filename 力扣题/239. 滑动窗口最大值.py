# @Time    : 2022/2/19 11:22
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 239. 滑动窗口最大值.py
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        # 我们存储的是索引坐标
        for i in range(len(nums)):
            # 如果i >= k且最大值正好位于窗口左端，则将其移除
            if i >= k and i - k == queue[0]:
                queue.popleft()
            # 如果当前值比queue里面最后的值要大，则删除queue最后的值
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                # queue中的首位保证是最大值
                res.append(nums[queue[0]])
        return res


if __name__ == '__main__':
    nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    print(Solution().maxSlidingWindow(nums, k))
