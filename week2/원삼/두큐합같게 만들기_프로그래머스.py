from collections import deque

def solution(que1, que2):
    que1,que2 = deque(que1),deque(que2)
    t = len(que1)
    answer = 0  
    sum_1 = sum(que1)
    sum_2 = sum(que2)
    goal = (sum_1+sum_2)/2
    count = 0
    while que1 and que2 and count < 2*t: 
        # 하나 비면 else되게 ~ 어차피 하나만 goal달성하면 되는 문제 + 루프 되는거 방지를 위해 한번 자리 되돌아오면 
        if sum_1 < sum_2:      # sum을 계속하니 시간 초과 떠서 sum을 저장해놓고 사용
            move = que2.popleft()
            que1.append(move)
            sum_1 += move
            sum_2 -= move
            answer += 1
            count += 1
        elif sum_1 > sum_2:
            move = que1.popleft()
            que2.append(move)
            sum_2 += move
            sum_1 -= move
            answer += 1
        else:
            return answer
    else:
        return -1
            