# @Time    : 2021/11/20 0:22
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 21. 合并两个有序链表.py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #res是虚拟头结点
        res = ListNode(None)
        l3 = res
        # 大概原理就是
        # l3瞄准好   指向 l1、l2 头结点的值，谁的头小选择谁并且往前走一步，走完了，l3也要走一步，直到走完其中一条，再指向另外一条
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return res.next


if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    print(Solution().mergeTwoLists(l1, l2))
