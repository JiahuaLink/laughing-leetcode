from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxDistance = 0
        for i in range(len(nums)):
            if i > maxDistance:
                return False
            distance = nums[i]
            maxDistance = max(maxDistance, i + distance)

        return True


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    is_can = Solution().canJump(nums)
    print(is_can)
