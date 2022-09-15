"""
【叠积木】
题目:积木宽高相等，长度不等，每层只能放一个或拼接多个积木，每层长度相等，求最大层数，最少2层。
输入:给定积木的长度，以空格分隔，例如:3 6 6 3。
输出:如果可以搭建，返回最大层数，如果不可以返回-1。
"""
class Solution:
    def gethigh(self, width: str):
        width = width.split(" ")
        count = 0
        for i in width:
            if count < self.getFlow(width, int(i)):
                count = self.getFlow(width, int(i))
        print(count)



    def getFlow(self,ls, length:int):
        flow = 0
        ls.sort()
        slen = length
        t = ls
        for i in ls:

            del t[t.index(i)]
            slen -= int(i)
            for j in t:
                if int(j) < slen:
                    slen -= int(j)
                elif int(j) == slen or int(j) == length:
                    flow += 1
                else:
                    slen = length
                    break
        return flow

print(Solution().gethigh('1 2 4 3 6 7'))

