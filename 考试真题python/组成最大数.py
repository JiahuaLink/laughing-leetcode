"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数
"""
nums = input().split(",")
lens = len(nums)
for i in range(lens):
    for j in range(i+1,lens):
        if nums[i]+nums[j] < nums[j]+nums[i]:
            nums[i],nums[j] = nums[j],nums[i]
print("".join(nums))
