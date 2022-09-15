
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix.pop()

        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(n):
            temp = []
            # 倒序依次取每个子列表的i坐标的元素
            for j in range(m):
                temp.append(matrix[m-j-1][i])
            matrix.append(temp)
        for i in range(m):
            matrix.remove(matrix[0])


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    
    Solution().rotate(matrix)
    print(matrix)