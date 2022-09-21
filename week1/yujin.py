# programmers 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

answer = []

def dfs(maps,location,visit,m,n,cnt) :
    x = location[0]
    y = location[1]
    if x<0 or x>=n or y<0 or y>=m : return
    if x==n-1 and y==m-1 : 
        answer.append(cnt)
        return
    if (not visit[x][y]) and (maps[x][y] == 1):
        visit[x][y] = True
        dfs(maps,(x+1,y),visit,m,n,cnt+1)
        dfs(maps,(x-1,y),visit,m,n,cnt+1)
        dfs(maps,(x,y+1),visit,m,n,cnt+1)
        dfs(maps,(x,y-1),visit,m,n,cnt+1)

def solution(maps):
    location = (0,0)
    n = len(maps)
    m = len(maps[0])
    visit = [[False]*m for _ in range(n)]
    dfs(maps,location,visit,m,n,1)
    if len(answer) == 0 : return -1
    return min(answer)