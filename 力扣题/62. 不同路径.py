# @Time    : 2021/11/19 22:57
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 岛屿数量.py
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        path = []
        for i in range(m):
            path.append([1] * n)

        print(path)
        for i in range(1, m):

            for j in range(1, n):
                if path[m][n] > '0' and i != m and j != n:
                    self.dfs_path(path, i, j, m, n)

    def dfs_path(self, path, i, j, m, n):
        if i > m or j > n :
            return
        # 每遇到一个1就开启淹没模式，置为0
        path[i][j] = '0'
        self.dfs(path, i, j - 1)
        self.dfs(path, i + 1, j)
        self.dfs(path, i, j + 1)
        self.dfs(path, i - 1, j)


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
