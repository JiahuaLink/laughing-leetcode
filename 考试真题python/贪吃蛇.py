steps = input().split(" ")
MN = input().split(" ")
M=int(MN[0])
N=int(MN[1])
import sys
arr = [] ###定义空间
first=[] ##定义起始位置
for i in range(M):
    line = sys.stdin.readline().strip().split()
    arr.append(line)
print(arr)
for i in range(N):
    for j in range(N):
        if arr[i][j] == "H":
            first.append(i)
            first.append(j)
print(first)
direction = {
    'U':[-1,0],
    'D':[1,0],
    'L':[0,-1],
    'R':[0,1],
}
goStep = [0,-1]
snake = []
for s in range(len(steps)):
    item= steps[s]
    if item == 'G': ##当为G时
        step = [first[0]+goStep[0],first[1]+goStep[1]] ##下一个定点的坐标=初始位置+前进的位置
        if step[0] < 0 or step[1] < 0 or step[0] >= N or step[1] >= M: ##判断step是否超出边界
            break
        stepStr=arr[step[0]][step[1]] ##下一个定点的字符串
        if stepStr == "F": ##如果遇到食物
            arr[first[0]][first[1]] = "S" ##初始位置变蛇身
            arr[step[0]][step[1]]   = "H" ##走到F的位置变H
            snake.insert(0,first) ##加入蛇身
            first = step
        else:##如果遇到E/S
            length = len(snake)
            if length > 0 : ##至少有一个舌头
                tail = snake[length-1] ##snake里面最后一个左边
                arr[tail[0]][tail[1]] = "E" ##将蛇尾变成空
                snake.pop()
                arr[first[0]][first[1]] = "H" ##将原先的蛇头变蛇身
                snake.insert(0,first)
            else:
                arr[first[0]][first[1]] = "E"
            if stepStr == "S":
                break
            arr[step[0]][step[1]] = "H" ##将走过的地方变蛇头
            first = step
        print(arr)
    else:
        goStep = direction[item] ##如果不是G，进行转向
print(len(snake)+1)

