# @Time    : 2021/12/6 22:29
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 前序遍历.py
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        result = []

        def preOrder(root: TreeNode):
            if root == None:
                return
            preOrder(root.left)
            result.append(root.val)
            preOrder(root.right)

        preOrder(root)
        return result


if __name__ == '__main__':
    root = TreeNode(1,TreeNode(2,None),TreeNode(3,None))
    print(Solution().preorderTraversal(root))

