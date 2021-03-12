x = 1
y = 1
ant_stage = []
for i in range(10):
    ant_stage.append(list(map(int, input().split())))
while True:
    if ant_stage[x][y] == 0:
        ant_stage[x][y] = 9
    elif ant_stage[x][y] == 2:
        ant_stage[x][y] = 9
        break

    if ant_stage[x+1][y] == 1 and ant_stage[x][y+1] == 1:
        break
    elif x == 9 and y == 9:
        break

    if ant_stage[x][y+1] != 1:
        y += 1
    elif ant_stage[x+1][y] != 1:
        x += 1
for i in range(len(ant_stage)):
    for j in range(len(ant_stage[i])):
        print(ant_stage[i][j], end=' ') if j != 10-1 else print(ant_stage[i][j], end = '\n')