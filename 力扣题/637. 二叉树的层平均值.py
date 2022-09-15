# @Time    : 2022/2/22 23:28
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 637. 二叉树的层平均值.py
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        current_node = []
        if root:
            current_node = [root]
        else:
            return []
        while current_node:
            next_node = []
            tmp = []
            for node in current_node:
                val = node.val
                tmp.append(val)
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            result.append(tmp,len(current_node))
            current_node = next_node
        return result
tmp = [20,9]
current_node =[1,2]
print(sum(tmp) / len(current_node))