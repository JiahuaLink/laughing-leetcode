"""
输入3行，第一行为整数N，第二、三行表示两个长度为N的整形数组A和B。如果Ai==Bj则认为（i，j）为最佳配对。
所有的最佳配对在满足以下条件的情况下组成最佳配对集合：A和B中的各个元素最多在集合中出现一次。
例如，A =「5， 10， 11，12， 14」，B = 「8， 9 ，11， 11， 5」，配对集合为「（0，4），（2，2），（2，3）」，
因为在集合A中索引2出现了两次，所以上面的配对集合不是最佳配对集合。你的任务是修改B中的一个元素，使得最佳配对集合的元素最多。并输出最佳配对集合的数量。

"""

# -*- coding:utf-8 -*-
import sys

num = int(input())
a = input().split()[:num]
b = input().split()[:num]

count = 0
diff = 0
for i in a:
    if i in b:
        count += 1
    else:
        diff += 1
if diff == 0:
    print(count-1)
else:
    print(count+1)
