# @Time    : 2022/2/20 14:07
# @Author  : JiahuaLink
# @Email   : 840132699@qq.com
# @File    : 剑指 Offer 10- I. 斐波那契数列.py
import functools

class Solution():
    @staticmethod
    @functools.lru_cache()
    def fib(n):
        """斐波那契函数"""
        if n < 2:
            return n
        return Solution.fib(n - 2) + Solution.fib(n - 1)

@functools.lru_cache(maxsize=300)
def fibonacci(n):
    """斐波那契函数"""
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(45))
print(Solution.fib(45))
