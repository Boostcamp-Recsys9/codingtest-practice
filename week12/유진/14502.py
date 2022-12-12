# 연구소
import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
virus = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 2: 
            virus.append((i,j))

tmp = [i for i in range(N*M)]
cand_list = list(combinations(tmp,3))

max_cnt = 0
for cand in cand_list :
    a, b, c = cand
    ax, ay = a//M, a%M
    bx, by = b//M, b%M
    cx, cy = c//M, c%M

    tmp_board = copy.deepcopy(board)
    if tmp_board[ax][ay] == 0 and tmp_board[bx][by] == 0 and tmp_board[cx][cy] == 0:
        tmp_board[ax][ay] = 1
        tmp_board[bx][by] = 1
        tmp_board[cx][cy] = 1
    else : continue

    q = deque(virus)
    while(q): 
        x, y = q.popleft()
        for i in range(4): 
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if tmp_board[nx][ny] == 0 : 
                    tmp_board[nx][ny] = 2
                    q.append((nx,ny))
                # elif tmp_board[nx][ny] == 1 : continue

    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp_board[i][j] == 0: cnt +=1
    # print(cnt)
    if cnt > max_cnt : max_cnt = cnt

print(max_cnt)