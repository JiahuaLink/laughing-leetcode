# @Time    : 2022/2/27 14:24
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 130. 被围绕的区域——复习.py


from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        def dfs(board, i, j):
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return

            board[i][j] = '-'
            dfs(board,i+1,j)
            dfs(board,i-1,j)
            dfs(board,i,j+1)
            dfs(board,i,j-1)


        for i in range(row):
            dfs(board, i, 0)
            dfs(board, i, col - 1)

        for j in range(col):
            dfs(board, 0, j)
            dfs(board, 0, row - 1)


        for i in range(row):
            for j in range(col):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='-':
                    board[i][j]='O'

board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
