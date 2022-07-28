import sys

notebook_height, notebook_width, sticker_nums = map(int, sys.stdin.readline().split())
notebook = [[0] * notebook_width for _ in range(notebook_height)]

def rotate_sticker(sticker_height, sticker_width):
    tmp_sticker = [[0] * 10 for _ in range(10)]
    
    for i in range(sticker_height):
        for j in range(sticker_width):
            tmp_sticker[i][j] = sticker[i][j]

    for i in range(sticker_width):
        for j in range(sticker_height):
            sticker[i][j] = tmp_sticker[sticker_height-1-j][i]

    sticker_height, sticker_width = sticker_width, sticker_height
    return sticker_height, sticker_width
    
def attach_sticker(x, y):
    for i in range(sticker_height):
        for j in range(sticker_width):
            if notebook[x+i][y+j] == 1 and sticker[i][j] == 1:
                return False

    for i in range(sticker_height):
        for j in range(sticker_width):
            if sticker[i][j] == 1:
                notebook[x+i][y+j] = 1
    return True

for _ in range(sticker_nums):
    sticker_height, sticker_width = map(int, sys.stdin.readline().split())
    sticker = [[0]*10 for _ in range(10)]
    for i in range(sticker_height):
        input_line = list(map(int, sys.stdin.readline().split()))
        for j in range(sticker_width):
            sticker[i][j] = input_line[j]
            
    for rotation in range(4):
        is_put = False
        for x in range(notebook_height-sticker_height):
            if is_put:
                break
            for y in range(notebook_width-sticker_width):
                if attach_sticker(x, y):
                    is_put = True
                    break

        if is_put:
            break
        sticker_height, sticker_width = rotate_sticker(sticker_height, sticker_width)
print(notebook)
                    
# 1. 스티커를 그대로 빈 공간에
# 2. 스티커 붙이는 공간의 우선순위는 위, 왼쪽
# 3. 붙일 공간이 없으면 시계 방향으로 90도 회전 후 2단계 반복
# 4. 모든 방향을 했는데 없으면 해당 스티커 버림