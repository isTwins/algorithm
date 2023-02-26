import re

def solution(dartResult):
    answer = 0
    numbers = re.findall('\d+', dartResult)
    numbers = list(map(int, numbers))
    chars = re.findall('\D+', dartResult)
    for j in range(3):
        for char in chars[j]:
            if char == 'D':
                numbers[j] = numbers[j] ** 2
            elif char == 'T':
                numbers[j] = numbers[j] ** 3
            elif char == '*':
                if j > 0:
                    numbers[j-1] *= 2
                    numbers[j] *= 2
                else:
                    numbers[j] *= 2
            elif char == '#':
                numbers[j] = -numbers[j]
    return sum(numbers)
            