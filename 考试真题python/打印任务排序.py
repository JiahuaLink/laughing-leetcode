
"""
打印任务排序
"""
class Solution:
    def printOrder(self, l):
        l1 = [i for i in l]
        l_index = 0
        # 降序排序
        l.sort(reverse=False)
        print(l)
        # 用于存放排列大小顺序
        order_dict = {}
        for i in l:
            order_dict[l_index] = i
            l_index += 1
        order = []
        # 遍历原来的列表
        for i in l1:
            for k in order_dict:
                if i == order_dict[k]:
                    order.append(k)
                    del order_dict[k]
                    break
        return order


p = Solution()
print(p.printOrder(['ab','aab']))
