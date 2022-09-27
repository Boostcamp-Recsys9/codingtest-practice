# 2*len(q1) -> 3* 로 수정
# test 1번 케이스 반례) 
# [1,1,1,8,10,9] [1,1,1,1,1,1] 
# [10,9] [1,1,1,1,1,1,1,1,1,8] -> 4
# [9] [1,1,1,1,1,1,1,1,1,8,10] -> 1
# [9,1,1,1,1,1,1,1,1,1] [8,10] -> 9

from collections import deque
from itertools import combinations

def solution(queue1, queue2):
    q1,q2 = deque(queue1),deque(queue2)
    target = (sum(q1) + sum(q2)) /2
    limit = len(queue1)*3
    s1,s2= sum(q1),sum(q2)
    
    answer = 0
    cnt = 0
    while(s1!=target) : 
        if s1 > s2 : 
            n = q1.popleft()
            q2.append(n)
            s1 -= n
            s2 += n
        else : 
            n = q2.popleft()
            q1.append(n)
            s2 -= n
            s1 += n
        answer += 1 
        cnt += 1
        if cnt > limit : return -1
    return answer    
