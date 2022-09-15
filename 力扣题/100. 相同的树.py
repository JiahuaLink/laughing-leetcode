# @Time    : 2021/12/17 0:21
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 100. 相同的树.py
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left,p.left) and self.isSameTree(p.right,q.right)
            return False
        return False

if __name__ == '__main__':
    p = [1, 2, 3]
    q = [1, 2, 3]
    print(Solution().isSameTree(p, q))
