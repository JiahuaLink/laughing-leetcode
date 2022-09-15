"""
【找终点】
题目：给定一个正整数数组，最大为100个成员，从第一个成员开始，走到数组最后一个成员最少的步骤数。第一步必须从第一元素开始，1<=步长<len/2,
第二步开始以所在成员的数字走相应的步数，如果目标不可达返回-1，只输出最少的步骤数。
分析：第一步可以走 [1,len/2) 的任意一种，遍历所有情况，找到符合要求的最小步骤
"""

class Solution:
    def calculate_min(self, tasks: str) -> int:
        tasks = tasks.split(" ")
        print(tasks)
        flag = True
        for i in range(1,int(len(tasks)/2)):
            count = 1
            index = i
            while True:
                index += int(tasks[index])
                count += 1
                if index > (len(tasks) -1):
                    break
                elif index == (len(tasks) -1):
                    flag = True
                    break
                else:
                    flag = False
        if flag:
            return count
        else:
            return -1

p = Solution()
print(p.calculate_min("7 5 9 4 2 6 8 3 5 4 3 9"))

nums = input().split(" ")
res = float("inf")
len_arr = len(nums)
len_step = len(nums) // 2 + 1
for i in range(1, len_step):
    step = 1
    arr_index = i
    while (1):
        arr_index += int(nums[arr_index])
        step += 1
        if arr_index > len_arr - 1:
            break
        if arr_index == len_arr - 1:
            res = min(res, step)
            break

if (res == float("inf")):
    print(-1)
else:
    print(res)
