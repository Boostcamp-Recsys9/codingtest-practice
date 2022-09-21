from collections import deque

def arangetest(x,y,n,m):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def bfs(maps,n,m):
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    queue = deque()
    queue.append((0,0))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if arangetest(nx,ny,n,m):
                if maps[nx][ny]==1:
                    maps[nx][ny]=maps[x][y]+1
                    queue.append((nx,ny))
    return maps[-1][-1]
        

def solution(maps):
    answer = 0
    n=len(maps)
    m=len(maps[0])
    answer=bfs(maps,n,m)
    print(maps)
    if answer==1:
        answer=-1
    return answer