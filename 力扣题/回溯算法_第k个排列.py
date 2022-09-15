# @Time    : 2021/12/20 23:32
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 回溯算法.py
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        input = [i for i in range(1, n + 1)]
        global result
        global count
        result = []
        count = 0

        def trace(path: list, choice):
            global count
            global result
            if len(path) == len(input):
                count += 1
                if count == k:
                    result = [str(i) for i in path]
                    return
                else:
                    return
            for item in choice:
                if item in path: continue
                path.append(item)
                trace(path, choice)
                path.pop()

        trace([], input)
        return ''.join(result)


if __name__ == '__main__':
    n = 9
    k = 278621
    print(Solution().getPermutation(n, k))
