"""
输入一个数字n，如果n为偶数则除以2，若为奇数则加1或者减1，直到n为1，求最少次数

"""
import sys

n = int(sys.stdin.readline().strip("\n"))
for i in range(n):
    if n % 2 == 0:
        n = n / 2
    else:
        n =min((n + 1) / 2, (n - 1) / 2)
    if n == 1:
        break

print(i)
