"""
要求：1s 262144k
特定大小的停车场，数组cars[ ]表示，其中0代表有车，1代表无车，车辆大小不一，统计停车场最少可以停多少辆车，返回具体的数字。长度小于1000

输入：小车占一个车位（长度1），中车占两个车位（长度2），大车占三个车位（长度3）

输出：整形数字字符串，表示最少停车数目

eg:
输入：1,1,0,0,1,1,1,0,1
输出：3
"""
cars = '1,1,1,1,1,1,1,1,1,1,1'
cars = ("".join(i for i in (cars.split(",")))).split("0")  ##通过0分割成若干个1的列表
# print(cars)

num = 0  ##定义累加器
for i in cars:
    lennum = (len(i))  ##判断1的长度
    if lennum == 0:
        num = num
    elif not lennum % 3 and len != 0:  ##%取余
        num = num + lennum / 3
    elif lennum % 3:
        num = num + (lennum - lennum % 3) / 3 + 1
print(int(num))
