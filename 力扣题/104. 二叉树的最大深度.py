# @Time    : 2021/11/25 0:13
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 104. 二叉树的最大深度.py
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        global maxdepth
        maxdepth = 0

        def dfs_depth(root: TreeNode, depth=0):
            if root is None:
                return 0
            global maxdepth

            if root:
                depth += 1
            if root.left:
                dfs_depth(root.left, depth)
            if root.right:
                dfs_depth(root.right, depth)
            if not root.right or root.left:
                maxdepth = max(maxdepth, depth)


        if root:
            dfs_depth(root)

        return maxdepth


if __name__ == '__main__':
    pass
