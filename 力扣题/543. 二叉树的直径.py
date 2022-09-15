# @Time    : 2022/2/23 22:29
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 543. 二叉树的直径.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """首先我们知道一条路径的长度为该路径经过的节点数减一，所以求直径（即求路径长度的最大值）等效于求路径经过节点数的最大值减一。"""
        self.ans = 1

        def dfs(node: TreeNode):
            if node is None:
                return 0

            L = dfs(node.left)
            R = dfs(node.right)

            # 下钻 一直到尽头  此时L R会返回0
            self.ans = max(self.ans, L + R) + 1
            return max(L, R) + 1

        dfs(root)

        return self.ans
a = TreeNode()

Solution().diameterOfBinaryTree()