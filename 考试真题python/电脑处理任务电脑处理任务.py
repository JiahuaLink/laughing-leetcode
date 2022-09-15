"""
【任务调度】
给出一些任务编号（比如2,2,2,3），再给一个任务冷却时间n（比如2），每个任务耗费一个单位的时间， 每个任务做完后需要冷却n个时间才能进行下一个相同编号的任务，冷却时间可以做编号不同的任务，计算所有任务完成的时间
如果任务编号是2,2,2,3  冷却时间是2，那么最后的总时间是7

"""
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # 统计每个任务出现的频次
        ct = Counter(tasks) # Counter({'A': 3, 'B': 3})
        # 获得出现频次最高的任务的频次
        # 输出次数最多的前一个 ct.most_common(1) 返回一个列表[("A",3)]，ct.most_common(1)[0]表示取列表第一个元素（"A",3）
        nbucket = ct.most_common(1)[0][1] # 3
        # 计算频次最高的任务一共有几个
        last_bucket_size = list(ct.values()).count(nbucket) # 2
        # 如任务总类和数量不足，需计算等待时间 ，总时间为矩形面积(max_count - 1) * (n + 1) + last_size * 1
        # (max_count - 1) * (n + 1): 频次最高的任务的数量max_count * 每轮时间(n + 1)。
        # max_count需减1，因为最后一轮可能不满，单独计算
        # last_size： 最后一轮中，仅需要处理频次最高的几个任务，其他任务或者在之前已经完成了，或者数量太多，变为以下第二种情况

        res = (nbucket - 1) * (n + 1) + last_bucket_size
        return max(res, len(tasks))

p = Solution()
print(p.leastInterval(["A","A","A","B","B","B"],2))