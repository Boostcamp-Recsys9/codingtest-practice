from collections import deque
from itertools import combinations

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    target = (sum(q1) + sum(q2)) /2
    limit = len(queue1)*2
    
    answer = 0
    cnt = 0
    while(sum(q1)!=target) : 
        if sum(q1) > sum(q2) : 
            n = q1.popleft()
            q2.append(n)
        else : 
            n = q2.popleft()
            q1.append(n)
        answer += 1 
        cnt += 1
        if cnt > limit : return -1
    return answer    