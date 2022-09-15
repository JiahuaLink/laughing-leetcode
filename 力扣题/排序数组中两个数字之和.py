# @Time    : 2021/11/13 0:24
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 排序数组中两个数字之和.py
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        j = len(numbers)-1
        i = 0
        while i < j:
            sum = numbers[i] + numbers[j]

            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            elif sum == target:
                return [i, j]


if __name__ == '__main__':
    numbers = [-1,0]
    target = -1
    print(Solution().twoSum(numbers, target))
