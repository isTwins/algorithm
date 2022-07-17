import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())    # 사무실의 크기

officeBoard = []    # 사무실 cctv 정보를 담을 리스트
watchBoard = []    # cctv가 감시하는 영역을 계산하기 위한 리스트
cctvQueue = deque()    # cctv 좌표를 넣기위한 큐
answer = 0

way = 0    # 감시 방향을 나타내기 위한 변수
dirX = [1, 0, -1, 0]
dirY = [0, 1, 0, -1]

# cctv가 감시하는 영역을 탐색하기 위한 함수
def calculatingArea(x, y, way):
    way %= 4    # 방향이 4방향이기 때문에 way 값이 3을 넘어갈 경우에 바꿔주기 위함
    # 사무실의 범위를 벗어나거나 벽을 만나기 전까지 감시하는 범위를 7로 바꿔주는 반복문
    while True:
        x += dirX[way]
        y += dirY[way]
        if x < 0 or x >= n or y < 0 or y >= m or boardCopy[x][y] == 6:
            return
        if boardCopy[x][y] != 0:
            continue
        boardCopy[x][y] = 7

# 사무실 cctv 위치 입력
for i in range(n):
    officeBoard.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if officeBoard[i][j] != 0 and officeBoard[i][j] != 6:
            cctvQueue.append((i, j))
        if officeBoard[i][j] == 0:
            answer += 1

cctvCount = cctvQueue.__len__()    # cctv 개수
            
for tmp in range(4**cctvCount):
    boardCopy = [item[:] for item in officeBoard]    # 이중 리스트 깊은 복사 deepcopy 대신 slicing을 한 이유는 더 빠르기 때분
    # 39부터 43줄은 4진수로 표현하기 위한 코드
    brute = tmp
    for i in range(cctvCount):
        way = brute % 4
        brute //= 4
        
        x, y = cctvQueue[i][0], cctvQueue[i][1]
        
        if officeBoard[x][y] == 1:
            calculatingArea(x, y, way)
            
        elif officeBoard[x][y] == 2:
            calculatingArea(x, y, way)
            calculatingArea(x, y, way+2)
            
        elif officeBoard[x][y] == 3:
            calculatingArea(x, y, way)
            calculatingArea(x, y, way+1)
            
        elif officeBoard[x][y] == 4:
            calculatingArea(x, y, way)
            calculatingArea(x, y, way+1)
            calculatingArea(x, y, way+2)
            
        elif officeBoard[x][y] == 5:
            calculatingArea(x, y, way)
            calculatingArea(x, y, way+1)
            calculatingArea(x, y, way+2)
            calculatingArea(x, y, way+3)
            
    tmpVal = 0    # 각 경우의 수마다 감시하지 못하는 영역을 담아두기 위한 변수
    for i in range(n):
        for j in range(m):
            if boardCopy[i][j] == 0:
                tmpVal += 1
                
    answer = min(answer, tmpVal)
    
print(answer)