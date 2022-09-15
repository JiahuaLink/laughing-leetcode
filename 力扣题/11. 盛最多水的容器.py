# @Time    : 2022/2/19 12:02
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 11. 盛最多水的容器.py
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxarea = 0
        left = 0
        right = len(height) - 1
        while left < right:

            cur_area = min(height[left], height[right]) * (right - left)
            maxarea = max(maxarea, cur_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxarea


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
