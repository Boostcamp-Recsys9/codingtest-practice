from collections import deque

dx=[0,0,-1,1]
dy=[1,-1,0,0]
    
def bfs(n,m,maps):
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if not (nx<0 or nx>=n or ny<0 or ny>=m) : 
                if maps[nx][ny]==1 :
                    maps[nx][ny]=maps[x][y]+1
                    queue.append((nx,ny))
    return maps[-1][-1]

def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = bfs(n,m,maps)
    if answer == 1 : return -1
    return answer