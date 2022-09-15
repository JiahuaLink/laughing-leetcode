class Solution(object):
    # def search(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     low = 0
    #     high = len(nums)-1
    #
    #     while low <= high:
    #         mid = int((high+low)/2)
    #         if target == nums[mid]:
    #             return mid
    #         if target > nums[mid]:
    #             low = mid + 1
    #         if target < nums[mid]:
    #             high = mid - 1
    #     return -1

    def bin_search(self, nums: list, target):
        i = 0
        j = len(nums) - 1

        while i <= j:

            mid = int((j + i) / 2)

            if target > nums[mid]:
                i = mid + 1
            elif target < nums[mid]:
                j = mid - 1

            elif target == nums[mid]:
                return mid

        return -1

    def firstBadVersion(self, n):
        """278. 第一个错误的版本
        :type n: int
        :rtype: int
        """



if __name__ == '__main__':
    nums = [5]
    target = 5
    print(Solution().bin_search(nums, target))
