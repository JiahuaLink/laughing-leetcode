# @Time    : 2021/12/24 23:19
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 98. 验证二叉搜索树.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        if root is None:
            return True

        def inOrder(root: TreeNode):
            if root is None:
                return
            inOrder(root.left)
            result.append(root.val)
            inOrder(root.right)

        inOrder(root)
        for i in range(len(result) - 1):
            if result[i] >= result[i + 1]:
                return False
        return True
