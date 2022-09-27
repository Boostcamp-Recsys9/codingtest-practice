# 코딩테스트 연습 > 2022 KAKAO TECH INTERNSHIP > 행렬과 연산
# https://school.programmers.co.kr/learn/courses/30/lessons/118670

# 채점 결과
# 정확성: 25.0
# 효율성: 16.7
# 합계: 41.7 / 100.0

import copy

def shiftrow(rc) : 
    rc.insert(0,rc.pop())
    return rc

def rotate(rc) : 
    new_rc = copy.deepcopy(rc)
    r = len(rc)
    c = len(rc[0])
    for i in range(r) : 
        for j in range(c) : 
            if i==0 : 
                if j == 0 : new_rc[i][j] = rc[i+1][j]
                else : new_rc[i][j] = rc[i][j-1]
            elif i== r-1 : 
                if j == c-1 : new_rc[i][j] = rc[i-1][j]
                else : new_rc[i][j] = rc[i][j+1]
            else : 
                if j == 0 : new_rc[i][j] = rc[i+1][j]
                elif j == c-1 : new_rc[i][j] = rc[i-1][j]
    return new_rc
            
def solution(rc, operations):
    for op in operations : 
        if op == "ShiftRow" : 
            rc = shiftrow(rc)
        else : 
            rc = rotate(rc) 
    return rc