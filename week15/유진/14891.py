import sys
from collections import deque

gear = [deque(sys.stdin.readline().rstrip()) for _ in range(4)]
gear.insert(0,[])
K = int(input())

def rotate(idx,dir) : 
    if dir == 1 : gear[idx].appendleft(gear[idx].pop())
    elif dir == -1 : gear[idx].append(gear[idx].popleft())
    return

def start(idx,dir) : 
    if idx-1 > 0 and gear[idx-1][2] != gear[idx][6] : turnleft(idx-1,-1*dir)
    if idx+1 < 5 and gear[idx+1][6] != gear[idx][2] : turnright(idx+1,-1*dir)
    rotate(idx, dir)
    return 
    
def turnleft(idx,dir) :
    if idx-1 > 0 and gear[idx-1][2] != gear[idx][6] : turnleft(idx-1,-1*dir)
    rotate(idx,dir)
    return

def turnright(idx,dir) :
    if idx+1 < 5 and gear[idx+1][6] != gear[idx][2] : turnright(idx+1,-1*dir)
    rotate(idx,dir)        
    return 
    
for i in range(K) :
    idx, dir = map(int,sys.stdin.readline().split())
    start(idx,dir)

# ans = 0
# for i in range(4) : 
#     if gear[i][0] : ans += 2**i
ans = int(gear[1][0])*1 + int(gear[2][0])*2 + int(gear[3][0])*4 + int(gear[4][0])*8 
print(ans)