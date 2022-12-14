# @Time    : 2022/2/18 20:34
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 60. 排列序列.py
"""
举例来说明。

n = 4， 参与排列的数字「1， 2， 3， 4」

列出所有的排列

1 + (permutations of 2, 3, 4)

2 + (permutations of 1, 3, 4)

3 + (permutations of 1, 2, 4)

4 + (permutations of 1, 2, 3)

n个数字的排列数为n!,那么3个数的排列数为6。假如k=14，那么第14个排列落在

3 + (permutations of 1, 2, 4)

令k=14-1(减去1是因为程序中索引从0开始), k/(n-1)!= 13/(4-1)! = 2, 在数列「1， 2， 3， 4」中索引为2的数字为3，所以第一个数字为3。

那么问题进一步缩小为「1， 2， 4」数字的排列，求第 k= k%(n-1)!=13%(4-1)=1 个排列：

1 + (permutations of 2, 4)

2 + (permutations of 1, 4)

4 + (permutations of 1, 2)

在这一步中，2个数字排列有2!， 总共有3*2!=6个，我们寻找第一个排列，那么落在

1 + (permutations of 2, 4)

此时 k/(n-2)! = 1/(4-2)! = 0, 即「1， 2， 4」中索引0的数字1。目前我们知道前面两个数字3，1。剩下的数字依次类推。

「2, 4」

k = k % (n-2)! = 1%(4-2)! = 1，第三个数字在「2， 4」中的索引为 k/(n-3)!= 1/(4-3)! = 1，所以第三个数字为4

「2」

k = k % (n-3)! = 1%(4-3)! = 0，第四个数字在「2」中的索引为 k/(n-4)!= 0/(4-4)! = 0，所以第四个数字为2

作者：a-bai-152
链接：https://leetcode-cn.com/problems/permutation-sequence/solution/golang-100-faster-by-a-bai-152/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        tokens = [str(i) for i in range(1, n+1)]
        res = ''
        k = k-1
        while n > 0:
            n -= 1
            a, k = divmod(k, math.factorial(n))
            res += tokens.pop(a)
        return res