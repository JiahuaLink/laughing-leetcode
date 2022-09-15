# @Time    : 2021/11/21 22:33
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 876. 链表的中间结点.py
# 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
#
# 如果有两个中间结点，则返回第二个中间结点。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        p = head
        q = head
        while q and q.next:
            q = q.next.next
            p = p.next
        return p


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, None)))
    print(Solution().middleNode(head).val)
