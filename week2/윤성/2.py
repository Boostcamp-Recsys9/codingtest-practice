from collections import deque

def change(big,small,big_sum,small_sum,stack):
    value=big.popleft()
    small.append(value)
    big_sum-=value
    small_sum+=value
    stack+=1

def solution(queue1, queue2):
    answer = 0
    queue1=deque(queue1)
    queue2=deque(queue2)
    length1=len(queue1)
    length2=len(queue2)
    sum1=sum(queue1)
    sum2=sum(queue2)
    stack1=0
    stack2=0
    while True:
        if stack1>=length1 and stack2>=length2:
            answer=-1
            break
        else:
            if sum1>sum2:
                change(queue1,queue2,sum1,sum2,stack1)
                answer+=1
            elif sum2>sum1:
                value=queue2.popleft()
                queue1.append(value)
                sum2-=value
                sum1+=value
                answer+=1
                stack2+=1
            else:
                break
    return answer