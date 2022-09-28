from collections import deque

def solution(rc, operations):
    answer = [[]]
    for contents in operations:
        if contents =="ShiftRow":
            rc=shiftrow(rc)
        else:
            rc=rotate(rc)
    return rc

def shiftrow(rc):
    temp=rc.pop(-1)
    rc.insert(0,temp)
    return rc
def rotate(rc):
    n=len(rc[0])
    m=len(rc)
    queue=deque()
    for i in range(1,m):
        queue.append(rc[i][0])
    for i in range(1,n-1):
        queue.append(rc[m-1][i])
    for i in range(m-1,0,-1):
        queue.append(rc[i][n-1])
    for i in range(n-1,-1,-1):
        queue.append(rc[0][i])
    for i in range(0,m):
        rc[i][0]=queue.popleft()
    for i in range(1,n-1):
        rc[m-1][i]=queue.popleft()
    for i in range(m-1,0,-1):
        rc[i][n-1]=queue.popleft()
    for i in range(n-1,0,-1):
        rc[0][i]=queue.popleft()
    return rc
        
    
        
    