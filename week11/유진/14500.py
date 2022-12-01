# 14500번 - 테트로미노
import sys

N, M = map(int, input().split())  #세로, 가로
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def tt1(start_pos):
    tt1_max = 0
    x,y = start_pos
    #세로
    tt1_sum = 0
    if 0 <= x+3 < N:
        for i in range(4) :
            tt1_sum += board[x+i][y]
    if tt1_max < tt1_sum : tt1_max = tt1_sum
    #가로
    tt1_sum = 0
    if 0 <= y+3 < M:
        for j in range(4):
            tt1_sum += board[x][y+j]
    if tt1_max < tt1_sum : tt1_max = tt1_sum
    return tt1_max

def tt2(start_pos):
    tt2_max = 0
    x,y = start_pos
    #가로, 세로 동일
    tt2_sum = 0
    if 0 <= x+1 < N  and 0 <= y+1 < M:
        for i in range(2):
            for j in range(2):
                tt2_sum += board[x+i][y+j]
    if tt2_max < tt2_sum : tt2_max = tt2_sum
    return tt2_max

def tt3(start_pos):
    tt3_max = 0
    x,y = start_pos
    #original
    tt3_sum = 0
    if 0 <= x+2 < N and 0 <= y+1 < M:
        for i in range(3):
            tt3_sum += board[x+i][y]
        tt3_sum += board[x+2][y+1]
    if tt3_max < tt3_sum : tt3_max = tt3_sum
    #반시계 90'
    tt3_sum = 0
    if 0 <= x-1 < N and 0 <= y+2 < M:
        for j in range(3):
            tt3_sum += board[x][y+j]
        tt3_sum += board[x-1][y+2]
    if tt3_max < tt3_sum : tt3_max = tt3_sum
    #반시계 180'
    tt3_sum = 0
    if 0 <= x+2 < N and 0 <= y+1 < M:
        for j in range(2):
            tt3_sum += board[x][y+j]
        for i in range(1,3):
            tt3_sum += board[x+i][y+1]
    if tt3_max < tt3_sum : tt3_max = tt3_sum
    #반시계 270'
    tt3_sum = 0
    if 0 <= x+1 < N and 0 <= y+2 < M:
        for j in range(3):
            tt3_sum += board[x][y+j]
        tt3_sum += board[x+1][y]
    if tt3_max < tt3_sum : tt3_max = tt3_sum
    #좌우반전
    tt3_sum = 0
    if 0 <= x+2 < N and 0 <= y-1 < M:
        for i in range(3):
            tt3_sum += board[x+i][y]
        tt3_sum += board[x+2][y-1]
    if tt3_max < tt3_sum : tt3_max = tt3_sum
    #반시계 90'
    tt3_sum = 0
    if 0 <= x+1 < N and 0 <= y+2 < M:
        for j in range(3):
            tt3_sum += board[x][y+j]
        tt3_sum += board[x+1][y+2]
    if tt3_max < tt3_sum : tt3_max = tt3_sum
    #반시계 180'
    tt3_sum = 0
    if 0 <= x+2 < N and 0 <= y+1 < M:
        tt3_sum += board[x][y+1]
        for i in range(3):
            tt3_sum += board[x+i][y]
    if tt3_max < tt3_sum : tt3_max = tt3_sum
    #반시계 270'
    tt3_sum = 0
    if 0 <= x+1 < N and 0 <= y+2 < M:
        tt3_sum += board[x][y]
        for j in range(3):
            tt3_sum += board[x+1][y+j]
    if tt3_max < tt3_sum : tt3_max = tt3_sum

    return tt3_max

def tt4(start_pos): 
    tt4_max = 0
    x,y = start_pos
    #original
    tt4_sum = 0
    if 0 <= x+2 < N and 0 <= y+1 < M:
        for i in range(2):
            tt4_sum += board[x+i][y]
        tt4_sum += board[x+1][y+1]
        tt4_sum += board[x+2][y+1]
    if tt4_max < tt4_sum : tt4_max = tt4_sum
    #반시계 90'
    tt4_sum = 0
    if 0 <= x-1 < N and 0 <= y+2 < M:
        for j in range(2):
            tt4_sum += board[x][y+j]
        tt4_sum += board[x-1][y+1]
        tt4_sum += board[x-1][y+2]
    if tt4_max < tt4_sum : tt4_max = tt4_sum
    #좌우반전
    tt4_sum = 0
    if 0 <= x+2 < N and 0 <= y-1 < M:
        for i in range(2):
            tt4_sum += board[x+i][y]
        tt4_sum += board[x+1][y-1]
        tt4_sum += board[x+2][y-1]
    if tt4_max < tt4_sum : tt4_max = tt4_sum
    #반시계 90'
    tt4_sum = 0
    if 0 <= x+1 < N and 0 <= y+2 < M:
        for j in range(2):
            tt4_sum += board[x][y+j]
        tt4_sum += board[x+1][y+1]
        tt4_sum += board[x+1][y+2]
    if tt4_max < tt4_sum : tt4_max = tt4_sum
    return tt4_max

def tt5(start_pos):
    tt5_max = 0
    x,y = start_pos
    #original
    tt5_sum = 0
    if 0 <= x+1 < N and 0 <= y+2 < M:
        for j in range(3):
            tt5_sum += board[x][y+j]
        tt5_sum += board[x+1][y+1]
    if tt5_max < tt5_sum : tt5_max = tt5_sum
    #반시계 90'
    tt5_sum = 0
    if 0 <= x+2 < N and 0 <= y+1 < M:
        for i in range(3):
            tt5_sum += board[x+i][y]
        tt5_sum += board[x+1][y+1]
    if tt5_max < tt5_sum : tt5_max = tt5_sum
    #반시계 180'
    tt5_sum = 0
    if 0 <= x-1 < N and 0 <= y+2 < M:
        for j in range(3):
            tt5_sum += board[x][y+j]
        tt5_sum += board[x-1][y+1]
    if tt5_max < tt5_sum : tt5_max = tt5_sum
    #반시계 270'
    tt5_sum = 0
    if 0 <= x+2 < N and 0 <= y-1 < M:
        for i in range(3):
            tt5_sum += board[x+i][y]
        tt5_sum += board[x+1][y-1]
    if tt5_max < tt5_sum : tt5_max = tt5_sum
    return tt5_max

answer = 0
for i in range(N) : 
    for j in range(M) : 
        res1 = tt1((i,j))
        res2 = tt2((i,j))
        res3 = tt3((i,j))
        res4 = tt4((i,j))
        res5 = tt5((i,j))
        tmp = max([res1,res2,res3,res4,res5])
        if answer < tmp : answer = tmp
print(answer)