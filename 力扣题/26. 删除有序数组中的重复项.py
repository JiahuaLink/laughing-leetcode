# @Time    : 2022/2/26 19:16
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 26. 删除有序数组中的重复项.py
"""双指针

首先注意数组是有序的，那么重复的元素一定会相邻。

要求删除重复元素，实际上就是将不重复的元素移到数组的左侧。

考虑用 2 个指针，一个在前记作 p，一个在后记作 q，算法流程如下：

1.比较 p 和 q 位置的元素是否相等。

如果相等，q 后移 1 位
如果不相等，将 q 位置的元素复制到 p+1 位置上，p 后移一位，q 后移 1 位
重复上述过程，直到 q 等于数组长度。

返回 p + 1，即为新数组长度。

作者：max-LFszNScOfE
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shuang-zhi-zhen-shan-chu-zhong-fu-xiang-dai-you-hu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0

        q = 1
        n = len(nums)
        while q < n:

            if nums[p] == nums[q]:

                q += 1
            elif nums[p] != nums[q]:
                nums[p + 1] = nums[q]
                p += 1
                q += 1
        return p + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(nums))
