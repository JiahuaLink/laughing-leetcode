"""
给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j] 不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。如果没有不包含相同字符的一对字符串，返回 0。
https://leetcode-cn.com/problems/maximum-product-of-word-lengths/submissions/
————————————————
版权声明：本文为CSDN博主「Aimee_c」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Aimee_c/article/details/120008193
"""

words = input().split(",")
res = 0
lens = len(words)
for i in range(lens):
    for j in range(i+1,lens):
        if not set(words[i]) & set(words[j]):
            res = max(res,len(words[i]) * len(words[j]))
print(res)
