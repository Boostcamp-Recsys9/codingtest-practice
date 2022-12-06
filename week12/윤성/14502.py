from itertools import combinations
from copy import deepcopy
from collections import deque

def range_check(x,y,n,m):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def bfs(virus,array):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    cnt=0
    queue = deque(virus)
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if range_check(nx,ny,n,m):
                if array[nx][ny] == 0:
                    array[nx][ny] = 1
                    cnt+=1
                    queue.append([nx,ny])
    return cnt
n,m=map(int,input().split())
array = []
virus=[]
area = []
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(m):
        if temp[j] == 2:
            virus.append([i,j])
        elif temp[j] == 0:
            area.append([i,j])
    array.append(temp)
walls = list(combinations(area,3))
answer=[]
for wall in walls:
    tmp_array = deepcopy(array)
    for contents in wall:
        tmp_array[contents[0]][contents[1]] = 1
    count = bfs(virus,tmp_array)
    answer.append(len(area)-count)
print(max(answer)-3)