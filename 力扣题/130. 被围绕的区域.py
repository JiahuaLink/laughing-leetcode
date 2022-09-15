# @Time    : 2022/2/20 23:10
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 130. 被围绕的区域.py
'''思路 把所有边界的O都找出来  与他相连的O全都换一个标记A，然后把所有未标记的O替换为X，'''
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])

        def dfs(board, i, j):
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return
            board[i][j] = '-'
            dfs(board, i - 1, j)
            dfs(board, i + 1, j)
            dfs(board, i, j - 1)
            dfs(board, i, j + 1)


        # 横 遍历第一行和最后一行
        for i in range(row):
            dfs(board, i, 0)
            dfs(board, i, col - 1)
        # 竖 遍历第一列和最后一列
        for j in range(col):
            dfs(board, 0, j)
            dfs(board, row - 1, j)

        # 遍历矩阵
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'
        return


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

Solution().solve(board)
print(board)
