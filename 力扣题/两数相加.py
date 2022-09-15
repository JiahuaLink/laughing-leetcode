class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __repr__(self):
    #     print(self.val)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r = re
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            # 除余
            carry = s // 10
            r.next = ListNode(s % 10)
            r = r.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        # 如果有进位  且l1 l2灭有下一节点时 那新的一位结点就为1
        if carry > 0:
            r.next = ListNode(1)
        return re.next

    def add_two_listnode(self, l1: ListNode, l2: ListNode):
        #
        result = ListNode(0)
        p_node = result
        carry = 0
        while (l1 or l2):
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = a + b + carry
            carry = sum // 10

            p_node.next = ListNode(sum % 10)
            p_node = p_node.next

            if l1 != None: l1 = l1.next
            if l2 != None: l2 = l2.next

        if carry > 0:
            p_node.next = ListNode(1)
        return result.next


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = [4, 5, 6, 7]

    l1 = ListNode(list1[0])
    l2 = ListNode(list2[0])
    # 当前指向节点 p指针
    p1 = l1
    p2 = l2
    for i in list1[1:]:
        # 指向下一个节点
        p1.next = ListNode(i)
        p1 = p1.next
    p2 = l2
    for i in list2[1:]:
        # 指向下一个节点
        p2.next = ListNode(i)
        p2 = p2.next
    result_listnode = Solution().add_two_listnode(l1, l2)
    print(result_listnode)
