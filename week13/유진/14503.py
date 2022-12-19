# 14503 : 로봇 청소기
import sys
# from collections import deque 
input = sys.stdin.readline
N,M = map(int,input().split())
r,c,dir = map(int,input().split()) # d: d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
board = [list(map(int,input().split())) for _ in range(N)]
# visit = [[0]*M for _ in range(N)]

cnt = 0
x,y = r,c

while(True):
    flag = 0 
    while (flag != 4): 
        # 1. 현재 위치를 청소한다.
        if board[x][y]==0 : 
            cnt += 1
            board[x][y] = 2
        #2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
        if dir==0:
            if board[x][y-1]==0:
                flag = 0
                y-=1
            else : flag += 1
            dir = 3
        elif dir==1:
            if board[x-1][y]==0:
                flag = 0
                x-=1
            else : flag += 1
            dir = 0
        elif dir==2: 
            if board[x][y+1]==0:
                flag = 0
                y+=1
            else : flag += 1
            dir = 1
        elif dir==3:
            if board[x+1][y]==0:
                flag = 0
                x+=1
            else : flag += 1
            dir = 2
    
    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    if dir==0: nx,ny = x+1,y
    elif dir==1: nx,ny = x,y-1
    elif dir==2: nx,ny = x-1,y
    elif dir==3: nx,ny = x,y+1
    
    if board[nx][ny] == 1: break # 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
    else : x,y = nx,ny

print(cnt)