""""
二叉树也可以用数组来村粗，给定一个数组，数的根节点的值存储在下标1，对于存储在下标N的节点，它的左子节点和右子节点分别存储在下表和2*N+1，并且我们用值-1
代表一个节点为空，给定一个数组存储的二叉树，试求从根节点到最小的叶子节点的路径，路径由节点的组组成
输入描述：
输入一行为数组的内容，数组的每个元素都是正整数，元素用空格分隔。注意第一个元素即为根节点的值，即数组的第N个元素对应的下边N，下标0在树的标识中没有使用，输入的数最多为7层
输出描述：
输出从根节点到最小叶子节点的路径，各个节点的值，由空格分割，用例保证最小叶子节点只有一个
输入 3 5 7 -1 -1 2 4
输出 3 7 2
3 5 7 1 1 2 4
3 7 1
"""


import sys
array1 = sys.stdin.readline().strip("\n").split(" ")
numlist = []
for i in array1:
    if int(i) > 0:
        numlist.append(i)
result = [numlist[0]]
for N in range(1,8):
    try:
        left = numlist[2*N]
        right = numlist[2*N+1]
    except:
        pass
    else:
        result.append(left)
        result.append(right)
print(" ".join(i for i in result))


