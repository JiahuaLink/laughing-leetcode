# @Time    : 2021/11/16 0:09
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 轮转数组.py


"""
189. 轮转数组
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。



示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-k :] + nums[:-k ]


if __name__ == '__main__':
    nums = [1, 2]
    k = 3
    print(-3%5)
    # print(nums[2:])
    # 输出[[3,99,-1,-100]]
    # Solution().rotate(nums, k)
    # print(nums)
