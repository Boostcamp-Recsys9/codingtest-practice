# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 불량 사용자
# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from itertools import permutations

def check(b_id,u_id):
    is_same = True
    if len(b_id)==len(u_id):
        for i in range(len(u_id)) :
            if b_id[i] == '*' : continue
            if b_id[i] != u_id[i] : 
                is_same = False
                break
    else : is_same = False
    return is_same
            
def solution(user_id, banned_id):
    answer = 0
    answerset = set()
    p = list(permutations(user_id,len(banned_id)))

    for u_id in p : 
        cnt = True
        for i in range(len(banned_id)) :
            if not check(banned_id[i], u_id[i]) : 
                cnt = False
                break
        if cnt :
            if set(u_id) not in answerset: 
                answerset.add(frozenset(u_id))
                answer += 1
            
    return answer