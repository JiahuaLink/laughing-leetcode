"""
有n个正整数组成的一个序列。给定正整数sum,求长度最长的连续子序列，使得他们的和等于sum。返回此子序列的长度，如果没有要求的序列，返回-1.

输入序列仅有数字和英文逗号构成，数字之间采用英文逗号分割
"""
nums = input().split(",")
sum = int(input())
res = {}  ##定义空字典
res[0] = -1  ###{0: -1}
ans = -1
preSum = 0  ##定义前n个元素之和
for index, num in enumerate(nums):
    preSum += int(num)  ##计算前n个元素之和
    if preSum not in res:
        res[preSum] = index  ##res={0: -1, 1: 0, 3: 1, 6: 2, 10: 3, 13: 4}
    diff = preSum - sum
    # print(preSum,sum,diff)
    if diff in res:
        ans = max(ans, index - res[diff])
print(ans)
