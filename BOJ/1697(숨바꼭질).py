import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
move = [-1] * 100001    # -1로 BFS를 위한 리스트 초기화

move[N] = 0    # 수빈이 시작하는 위치를 0으로 설정
pos = deque()    # 다음으로 이동할 위치를 넣을 큐
pos.append(N)    # 수빈이 위치 큐에 집어넣음

while move[K] == -1:    # 동생의 위치에 도달할 때까지 반복
    x = pos.popleft()    # 이동할 위치를 큐에서 뺌
    for dir in (x-1, x+1, x*2):    # 해당 위치의 -1, +1, 2배 위치로 이동
        if dir < 0 or dir > 100000: continue    # 다음으로 이동하는 위치가 음수로 가거나 100000을 넘는 경우 반복문 빠져나옴
        if move[dir] != -1: continue    # 다음으로 움직이는 위치의 값이 이미 방문한 곳이면 반복문 빠져나옴
        move[dir] = move[x] + 1    # 다음으로 이동하는 위치에 이전 위치의 값에 +1
        pos.append(dir)    # 다음으로 이동할 위치의 값을 큐에 집어넣음
        
print(move[K])