def solution(n):
    for i in range(3, n+1):
        if n % 2 == 1:
            answer = 2
            break
            
        if n % i == 1:
            answer = i
            break
    return answer