# @Time    : 2021/11/24 23:50
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 94. 二叉树的中序遍历.py
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result: list = []

        def inOrder(root: TreeNode):
            if root.val == None:
                return
            # 左
            inOrder(root.left)
            # 中
            result.append(root.val)

            # 右
            inOrder(root.right)

        inOrder(root)
        return result


if __name__ == '__main__':
    pass
