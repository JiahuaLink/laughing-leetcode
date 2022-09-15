"""
【装快递】
题目：一辆货车载重N,一批快递重量为{a,b,c,d,e…},求卡车能装的最多快递数？
分析：把快递按照重量排序，然后从最轻的开始加，一旦等于或者超出了卡车的重量，就break 然后输出快递数量就行

"""
class Solution:
    def getMastnum(self, N:int,things:str)->int:
        things = things.split(",")
        l = list(map(int, things))
        heigh = 0
        num = 0
        # 升序排序
        l.sort()
        for i in range(len(l)):
            heigh += int(l[i])
            if heigh <= N:
                num += 1
        return num


p = Solution()
print(p.getMastnum(20,"5,10,2,11"))
