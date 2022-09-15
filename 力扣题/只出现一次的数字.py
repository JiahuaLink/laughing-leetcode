# @Time    : 2021/11/13 0:00
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 只出现一次的数字.py
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_list = list(set(nums))
        count_result = []
        result = []
        for i in set_list:
            # 每个数出现的次数
            count = nums.count(i)
            if count == 1:
                result.append(i)
            count_result.append(count)
        if len(result) == 1:
            return result[0]
        if [1, 3] == (sorted(list(set(count_result)))):
            return result[0]


if __name__ == '__main__':
    nums = [2,2,3,2]
    print(Solution().singleNumber(nums))
