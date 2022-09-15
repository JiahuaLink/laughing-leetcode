# @Time    : 2022/2/13 17:30
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 剑指 Offer 04. 二维数组中的查找.py
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 列数
        m = len(matrix[0])
        # 行数
        n = len(matrix)

        for i in range(m):
            start = i
            while start < n:
                # 发射出当前行的所有列的数字 [0][0] [0][1]  [0][2] ..
                col_num = matrix[i][start]
                if col_num < matrix:
                    start += 1
                elif col_num ==target:
                    return True
                else:
                    # 发射出当前列的所有行的数字 [0][0] [1][0]  [3][0] ..
                    row_num = matrix[start][i]




if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
