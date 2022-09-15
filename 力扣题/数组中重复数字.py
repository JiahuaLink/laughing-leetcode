# @Time    : 2021/9/25 20:09
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 数组中重复数字.py

class Solution:

    def find_dup(self):
        """返回数组中重复的数字"""
        tmp = []
        array = [1, 5, 4, 7, 8, 9, 7, 9, 99]

        for i in range(0, len(array) - 1):
            print(array[i])


if __name__ == '__main__':
    result = Solution().find_dup()

