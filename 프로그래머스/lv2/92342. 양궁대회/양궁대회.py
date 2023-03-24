from itertools import product

def solution(n, info):
    answer = [0 for i in range(11)]
    max_score = 0
    info.reverse()
    for tf in product((True, False), repeat=11):
        arrows = 0
        arrows = sum(info[i]+1 for i in range(11) if tf[i])
        if arrows <= n:
            appeach = sum(i for i in range(11) if info[i] and not tf[i])
            ryan = sum(i for i in range(11) if tf[i])
            score_gap = ryan - appeach
            if max_score < score_gap:
                max_score = score_gap
                answer = [info[i]+1 if tf[i] else 0 for i in range(11)]
                answer[0] = n - arrows
            # elif max_score == score_gap:
            #     tmp = [info[i]+1 if tf[i] else 0 for i in range(11)]
            #     tmp[10] = n - arrows
            #     for i in reversed(range(10)):
            #         if tmp[i] > answer[i]:
            #             answer = tmp
            #             break
    answer.reverse()
    return [-1] if max_score == 0 else answer