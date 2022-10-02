from itertools import combinations_with_replacement
from copy import deepcopy

def solution(n, info):
    answer = []
    max_score = 0
    max_allow = [0 for _ in range(11)]
    score_table = [i for i in range(0,11)]
    cases = list(set(combinations_with_replacement(score_table,n)))
    for choice in cases:
        temp = [0 for _ in range(11)]
        for content in choice:
            temp[10-content]+=1
        temp_score = score_calculate(info,temp)
        if temp_score > max_score:
            max_allow = deepcopy(temp)
            max_score = temp_score
        elif temp_score == max_score:
            if same_calculate(max_allow,temp):
                max_allow = deepcopy(temp)
    answer = max_allow
    if max_score >0:
        return answer
    else:
        return [-1]

def score_calculate(info,cases):
    info_score=0
    cases_score=0
    for i in range(0,11):
        if info[i] < cases[i]:
            cases_score+=(10-i)
        elif info[i]> cases[i]:
            info_score+=(10-i)
        else:
            if cases[i] > 0:
                info_score+=(10-i)
    return cases_score-info_score
            
def same_calculate(info,cases):
    info_mul=0
    cases_mul=0
    for i in range(0,11):
        info_mul += info[i]*(10-i)
        cases_mul += cases[i] * (10-i)
    return info_mul >= cases_mul