mg = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

path = []
node = [1, 1, -1]
point = [3, 4]
flag = 0
path.append(node)

while True:
    mg[node[0]][node[1]] = 1
    
    if node[0] == point[0] and node[1] == point[1]:
        x = path.index(node)
        flag = 1
        break

    for i in range(4):
        if mg[node[0] + dx[i]][node[1] + dy[i]] == 0:
            path.append([node[0] + dx[i], node[1] + dy[i], path.index(node)])
        
    if path.index(node) == len(path) - 1:
        flag = 2
        break
    else:
        node = path[path.index(node) + 1]
    
re = []

if flag == 1:
    while x != -1:
        re.append((path[x][0], path[x][1]))
        x = path[x][2]
    
    for i in re[::-1]:
        print(i, ' ')

elif flag == 2:
    print("未找到迷宫路径。")
