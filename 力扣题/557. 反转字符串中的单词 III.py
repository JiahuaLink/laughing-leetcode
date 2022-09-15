# @Time    : 2021/11/21 22:06
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 557. 反转字符串中的单词 III.py
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = ''
        for word in words:
            ss = list(word)
            i = 0
            j = len(ss) - 1
            while i < j:
                ss[i], ss[j] = ss[j], ss[i]
                i += 1
                j -= 1
            result += ''.join(ss) +" "
        return result.rstrip()

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))
