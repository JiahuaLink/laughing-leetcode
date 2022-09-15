"""
要求：1s 262144k

某文件系统中有N个目录，每个目录都一个独一无二的ID。每个目录只有一个父目录，但每个父目录下可以有零个或者多个子目录，目录结构呈树状结构。
假设，根目录的ID为0，且根目录没有父目录，其他所有目录的ID用唯一的正整数表示，并统一编号。
现给定目录ID和其父目录ID的对应父子关系表[子目录ID，父目录ID]，以及一个待删除的目录ID，请计算并返回一个ID序列，表示因为删除指定目录后剩下的所有目录，返回的ID序列以递增序输出。
注意：
1、被删除的目录或文件编号一定在输入的ID序列中；
2、当一个目录删除时，它所有的子目录都会被删除。

输入描述: 输入的第一行为父子关系表的长度m；接下来的m行为m个父子关系对；最后一行为待删除的ID。序列中的元素以空格分割，参见样例。

输出描述: 输出一个序列，表示因为删除指定目录后，剩余的目录ID。
示例1
输入
5
8 6
10 8
6 0
20 8
2 6
8

输出
2 6

"""

n = int(input())
import sys
root = []
node = []
for i in range(n):
    line = sys.stdin.readline().strip().split()
    node.append(line[0]) ##定义子目录
    root.append(line[1]) ##定义父目录
rm_node=input()
index=[]
for i in range(len(node)):
    index.append(i)
dict_root = dict(zip(index, root))##定义索引和子目录的字典
dict_node = dict(zip(index, node))##定义索引和父目录的字典
pop_index = list(i for i in range(len(node)) if dict_root.get(i)==rm_node)

if rm_node in node and rm_node not in  root:
    res = list(set(node+root))
    res.remove(rm_node)
    res.remove('0')
    print(' '.join(str(x) for x in res))

if rm_node in root:
    for i in pop_index:
        del dict_node[i]
    new_node=list(set(list(dict_node.values())))
    new_root=list(set(root))
    new_root.remove(rm_node)

    if rm_node not in node:
        res=list(set((new_node + new_root)))
        res.remove('0')
        print(' '.join(str(x) for x in res))

    if rm_node  in node:
        new_node.remove(rm_node)
        res = list(set((new_node + new_root)))
        res.remove('0')
        print(' '.join(str(x) for x in res))
