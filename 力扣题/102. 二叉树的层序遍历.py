# @Time    : 2022/2/22 22:38
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 102. 二叉树的层序遍历.py
# Definition for a binary tree node.
"""其思路就是将二叉树的节点加入队列，出队的同时将其非空左右孩子依次入队，出队到队列为空即完成遍历。"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        if root:
            # 首先获取当前层级
            current_node = [root]

        else:
            return result

        # 当前层级有的话 开始向下查找子层级
        while current_node:
            # 用来装下一层级
            next_node = []
            tmp = []
            for node in current_node:
                val = node.val
                # 先把当前层级的装入 有可能是多个节点
                tmp.append(val)
                # 如果有下一层级 就装入next_node
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            result.append(tmp)
            current_node = next_node

        return result