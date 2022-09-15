# @Time    : 2021/11/21 22:00
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 167. 两数之和 II - 输入有序数组.py
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]


if __name__ == '__main__':
    numbers = [5, 25, 75]
    numbers.reverse()
    print(numbers)
    # target = 100
    # print(Solution().twoSum(numbers, target))
