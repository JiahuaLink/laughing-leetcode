"""
一个整数可以有连续的自然数之和来表示。给定一个整数，计算该整数有几种连续自然数之和的表达式，且打印出每种表达式。
输入:一个目标整数T（1<=T<=1000）
输出：该整数的所有表达式和表达式的个数。如果有多种表达式，输出要求为：
1.自然数个数最少的表达式优先输出
2.每个表达式中按自然数递增的顺序输出，具体格式参见样例。在每个测试数据结束时，输出一样“Resule：X”，其中X是最终的表达式个数。

eg:
输入
9
输出
9=9
9=4+5
9=2+3+4
Result：3
"""

num = int(input())
sum = 0
for i in range(1, int(num/2)):
    if(2 * num % i == 0):
        t = 2*num/i-i+1
        if (t % 2 == 0):
            k = int(t/2)
            res = list(str(x) for x in range(k,k+i))
            # print(res)
            if len(res) == 1:
                print(str(num)+"="+str(num))
                sum += 1
            else:
                print(str(num)+"=" + "+".join(res))
                sum += 1
print("Result:"+str(sum))
