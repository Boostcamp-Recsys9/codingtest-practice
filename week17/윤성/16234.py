import sys
from collections import deque


# def range_check(x,y,n):
#     if 0<=x<n and 0<=y<n:
#         return True
#     return False

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    union_country = [(x,y)]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <=abs(graph[x][y]-graph[nx][ny]) <= r:
                    visited[ny][ny] = True
                    queue.append((nx,ny))
                    union_country.append((nx,ny))
    return union_country

input = sys.stdin.readline
n,l,r = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = []
answer=0
for i in range(n):
    graph.append(list(map(int,input().split())))

while True:
    visited = [[False]*n for _ in range(n)]
    move_flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                union_country = bfs(i,j)
                if 1 < len(union_country):
                    move_flag=True
                    population_average = sum([graph[x][y] for x,y in union_country]) // len(union_country)
                    for x,y in union_country:
                        graph[x][y] = population_average
    if not move_flag:
        break
    else:
        answer+=1
print(answer)