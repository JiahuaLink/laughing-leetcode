# @Time    : 2022/2/22 23:26
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 199. 二叉树的右视图.py
"""层序遍历的时候，判断是否遍历到单层的最后面的元素，如果是，就放进result数组中，随后返回result就可以了。"""
# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
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
            for i, node in enumerate(current_node):
                val = node.val
                # 先把当前层级的装入 有可能是多个节点 将当前层的最后一个节点放入结果列表
                if i == len(current_node) - 1:
                    result.append(node.val)

                # 如果有下一层级 就装入next_node
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)

            current_node = next_node

        return result