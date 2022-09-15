"""
停车场有一排车位，0表示没有停车，1表示有车，需要找到一个车位，使距离停车人的车最近的距距离是最大的，返回此时最大距离
输入：
1,0,0,0,0,1,0,0,1,0,1
输出
2
"""
inputLine = "".join(input().split(","))
line = inputLine.replace("010","01210").split("2")

res = []
for item in line:
    zeroLength = len("".join(item.split("1")))
    if item.startswith("1") and item.endswith("1"):
        length = (zeroLength+1) // 2
    else:
        length = zeroLength
    res.append(length)
print(max(res))
