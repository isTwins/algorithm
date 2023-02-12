def solution(n):
    answer = []
    str_n = list(str(n))
    for digit in str_n[::-1]:
        answer.append(int(digit))
    
    return answer