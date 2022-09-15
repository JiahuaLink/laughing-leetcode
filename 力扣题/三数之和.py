from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 先排序
        nums.sort()
        for i in range(len(nums)):
            # 左边从第一个开始遍历
            start = i+1
            # 右边指针从最后一个坐标
            # 开始
            end = len(nums)-1
            # 如果
            while start < end:
                # 如果刚好等于的话 就存入临时列表
                if nums[i]+nums[start]+nums[end] == 0:
                    temp = [nums[i], nums[start], nums[end]]
                    
                    # 去重的
                    if temp not in result:
                        result.append(temp)
                    start += 1
                    end -= 1
                # 如果相加的数字总和小于0  那么左指针往右边走
                elif nums[i]+nums[start]+nums[end] < 0:
                    start += 1

                # 反之右指针往前
                elif nums[i]+nums[start]+nums[end] > 0:
                    end -= 1
                # 两边相遇 不处理
            
                else:
                    pass
        
        return result
        

if __name__ == '__main__':
    nums =  [-1,0,1,2,-1,-4]
    result = Solution().threeSum(nums)
    print(result)
    