import sys

notebook_height, notebook_width, sticker_nums = map(int, sys.stdin.readline().split())
notebook = [[0] * notebook_width for _ in range(notebook_height)]

def rotate_sticker(sticker):
    sticker_height = len(sticker)
    sticker_width = len(sticker[0])
    tmp_sticker = [[0]*sticker_height for _ in range(sticker_width)]
    
    for i in range(sticker_height):
        for j in range(sticker_width):
            tmp_sticker[j][sticker_height-1-i] = sticker[i][j]

    sticker = tmp_sticker
    sticker_height, sticker_width = sticker_width, sticker_height
    return sticker, sticker_height, sticker_width
    
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
    sticker = []
    for i in range(sticker_height):
        sticker.append(list(map(int, sys.stdin.readline().split())))
            
    for rotation in range(4):
        is_put = False
        for x in range(notebook_height-sticker_height+1):
            if is_put:
                break
            for y in range(notebook_width-sticker_width+1):
                # print(x, y, sticker_height, sticker_width, sticker)
                if attach_sticker(x, y):
                    is_put = True
                    break

        if is_put:
            break
        sticker, sticker_height, sticker_width = rotate_sticker(sticker)

answer = 0
for i in range(notebook_height):
    for j in range(notebook_width):
        answer += notebook[i][j]

print(answer)