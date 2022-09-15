# @Time    : 2021/12/6 22:51
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : N 叉树的前序遍历.py
"""
# Definition for a Node.


"""
from typing import List


class Node:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def preOrder(root: 'Node'):
            if root == None:
                return
            result.append(root.val)
            for child in root.children:
                preOrder(child)
        preOrder(root)
        return result
