# @Time    : 2021/12/16 23:36
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 349. 两个数组的交集.py
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return [i for i in nums2 if i in nums1]


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(Solution().intersection(nums1,nums2))