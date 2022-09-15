from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        numss = []
        for i in nums:
            numss.append(i * i)
        return Solution.quick_sorted(numss)

    @staticmethod
    def quick_sorted(nums: list):
        if len(nums) < 2:
            return
        E = []
        L = []
        R = []

        p = nums[0]
        while len(nums) > 0:
            if nums[-1] < p:
                L.append(nums.pop())
            elif nums[-1] == p:
                E.append(nums.pop())
            else:
                R.append(nums.pop())
        Solution.quick_sorted(L)
        Solution.quick_sorted(R)
        nums.extend(L)
        nums.extend(E)
        nums.extend(R)

    @staticmethod
    def inplace_quick_sort(s, a, b):
        """
        选择索引b处的值为基准值
        通过从左到右扫描与从右到左扫描
        left是左扫描位置，right是右扫描位置
        找到左边第一个大于基准值的位置与右边第一个小于基准值的位置
        然后将这两个值交换，并将left向右移动，right向左移动
        继续重复进行 直到left>right,也就是全部扫描一遍后
        将基准值s[b]与最后的left位置交换
        这样就完成了分割 然后再进行递归调用两个序列
        """

        if a >= b:
            return
        # s[b]作为基准值
        p = s[b]
        # left和right相当于指向
        left = a
        right = b - 1

        while left <= right:

            while left <= right and s[left] < p:
                left += 1

            while left <= right and p < s[right]:
                right -= 1

            if left <= right:
                s[left], s[right] = s[right], s[left]
                left, right = left + 1, right - 1

        s[left], s[b] = s[b], s[left]
        Solution.inplace_quick_sort(s, a, left - 1)
        Solution.inplace_quick_sort(s, left + 1, b)


if __name__ == '__main__':
    nums = [-4, -1, 0, 3, 10, 9]
    (Solution.inplace_quick_sort(nums, 0, len(nums) - 1))
    print(nums)
