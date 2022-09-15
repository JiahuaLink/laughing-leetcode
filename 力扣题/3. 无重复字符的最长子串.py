# @Time    : 2021/11/21 23:08
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 3. 无重复字符的最长子串.py
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""
其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，这时候不满足要求。所以，我们要移动这个队列！

如何移动？

我们只要把队列的左边的元素移出就行了，直到满足题目要求！

一直维持这样的队列，找出队列出现最长的长度时候，求出解！

作者：powcai
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        # 最大长度
        max_len = 0
        # 当前实际长度
        cur_len = 0
        for i in range(n):
            cur_len += 1
            # 如果字符已经在集合里出现 那么就滑动窗口
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len

if __name__ == '__main__':
    s = 'abcabcbb'
    print(Solution().lengthOfLongestSubstring(s))
    [].sort()
