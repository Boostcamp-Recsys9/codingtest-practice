from collections import deque

def is_range(n,m,x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

def bfs(start,board):
    INF = int(1e9)
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    visit = [[INF] * len(board) for _ in range(len(board))]
    visit[0][0] = 0
    queue = deque([start])
    while queue:
        x,y,cost,direction = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if is_range(len(board),len(board),nx,ny) and board[nx][ny] == 0:
                if i==direction:
                    nc = cost+100
                else:
                    nc = cost+600
                if nc < visit[nx][ny]:
                    visit[nx][ny] = nc
                    queue.append((nx,ny,nc,i))
    return visit[-1][-1]

def solution(board):
    answer = 0
    answer = min(bfs((0,0,0,1),board),bfs((0,0,0,2),board))
    return answer