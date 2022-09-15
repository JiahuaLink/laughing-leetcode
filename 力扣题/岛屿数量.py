# @Time    : 2021/11/19 22:57
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 岛屿数量.py
class Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        # m, n = len(grid), len(grid[0])
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 看深度一轮到底直到遇到有海水的0才返回
                if grid[i][j] > '0':
                    counter += 1
                    self.dfs(grid, i, j)
        return counter

    def dfs(self, grid, i, j):
        # 停止条件
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        # 每遇到一个1就开启淹没模式，置为0
        grid[i][j] = '0'
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    print(Solution().numIslands(grid))