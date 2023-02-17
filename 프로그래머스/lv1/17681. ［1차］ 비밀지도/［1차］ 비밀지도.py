def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        line = bin(arr1[i] | arr2[i])[2:]
        answer.append(str(line).zfill(n).replace('1', '#').replace('0', ' '))
                
        
    return answer