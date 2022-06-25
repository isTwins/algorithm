import sys
from collections import deque

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
maze = []

# 지도 크기 입력
r, c = map(int, sys.stdin.readline().split())
for _ in range(r):
    maze.append(list(sys.stdin.readline().rstrip()))

fire = [[-1] * c for _ in range(r)]
escape = [[-1] * c for _ in range(r)]
queue_fire = deque()
queue_escape = deque()

# 미로를 돌면서 불위치는 queue_fire에 지훈은 queue_escape에 index를 넣어준다.
for i in range(r):
    for j in range(c):
        if maze[i][j] == 'F':
            queue_fire.append((i, j))
            fire[i][j] = 0
        if maze[i][j] == 'J':
            queue_escape.append((i, j))
            escape[i][j] = 0
            
# 불 확산속도 계산            
while queue_fire:
    x, y = queue_fire.popleft()
    for i in range(4):
        nx = x + dir_x[i]
        ny = y + dir_y[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if fire[nx][ny] == -1 and maze[nx][ny] != '#':
            fire[nx][ny] = fire[x][y] + 1
            queue_fire.append((nx, ny))

# 지훈이 도망 계산
while queue_escape:
    x, y = queue_escape.popleft()
    for i in range(4):
        nx = x + dir_x[i]
        ny = y + dir_y[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:    # 범위를 벗어났다는 것은 탈출에 성공했다는 것을 구분하기 위한 조건문
            print(escape[x][y] + 1)
            exit()
        if escape[nx][ny] == -1 and maze[nx][ny] == '.':
        # 화염보다 늦게 도착하는 경우 진행 못하는 조건 추가.
            if fire[nx][ny] == -1 or fire[nx][ny] > escape[x][y] + 1:
                escape[nx][ny] = escape[x][y] + 1
                queue_escape.append((nx, ny))
print("IMPOSSIBLE")