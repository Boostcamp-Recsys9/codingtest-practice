# 15683 : 감시
import sys
input = sys.stdin.readline
from itertools import product
import copy

sys.setrecursionlimit(10**5)
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
cctvs = []

# 1,2,3,4 -> 오른쪽, 아래, 왼쪽, 위
# 감시가능한 영역 : -1

def right(tmp_board,i,j) : 
    for k in range(j+1,M) :
        if tmp_board[i][k] == 6 : break
        elif tmp_board[i][k] == 0 : tmp_board[i][k] = -1
def down(tmp_board,i,j) : 
    for k in range(i+1,N) :
        if tmp_board[k][j] == 6 : break
        elif tmp_board[k][j] == 0 : tmp_board[k][j] = -1
def left(tmp_board,i,j) :
    for k in range(j-1,-1,-1) :
        if tmp_board[i][k] == 6 : break
        elif tmp_board[i][k] == 0 : tmp_board[i][k] = -1
def up(tmp_board,i,j) :
    for k in range(i-1,-1,-1) :
        if tmp_board[k][j] == 6 : break
        elif tmp_board[k][j] == 0 : tmp_board[k][j] = -1

def set_dir(dir,tmp_board,cctv):
    (i,j),cctv_type = cctv
    
    if cctv_type == 1 :
        if dir == 1 : # →
            right(tmp_board,i,j)
        elif dir == 2 : # ↓
            down(tmp_board,i,j)
        elif dir == 3 : # ←
            left(tmp_board,i,j)
        elif dir == 4 : # ↑
            up(tmp_board,i,j)
    
    elif cctv_type == 2 :
        if dir == 1 or dir == 3 : # ←→
            left(tmp_board,i,j)
            right(tmp_board,i,j)
        elif dir == 2 or dir == 4 : # ↑↓
            up(tmp_board,i,j)
            down(tmp_board,i,j)
    
    elif cctv_type == 3 :
        if dir == 1 : # ↑→
            up(tmp_board,i,j)
            right(tmp_board,i,j)
        elif dir == 2 : # →↓
            right(tmp_board,i,j)
            down(tmp_board,i,j)
        elif dir == 3 : # ←↓
            left(tmp_board,i,j)
            down(tmp_board,i,j)
        elif dir == 4 : # ←↑
            left(tmp_board,i,j)
            up(tmp_board,i,j)
    
    elif cctv_type == 4 :
        if dir == 1 : # ←↑→
            left(tmp_board,i,j)
            up(tmp_board,i,j)
            right(tmp_board,i,j)
        elif dir == 2 : # ↑→↓
            up(tmp_board,i,j)
            right(tmp_board,i,j)
            down(tmp_board,i,j)
        elif dir == 3 : # ←↓→
            left(tmp_board,i,j)
            down(tmp_board,i,j)
            right(tmp_board,i,j)
        elif dir == 4 : # ←↑↓
            left(tmp_board,i,j)
            up(tmp_board,i,j)
            down(tmp_board,i,j)
    
    elif cctv_type == 5 :
        left(tmp_board,i,j)
        up(tmp_board,i,j)
        right(tmp_board,i,j)
        down(tmp_board,i,j)
      

for i in range(N) :
    for j in range(M) :
        if board[i][j] : cctvs.append(((i,j),board[i][j]))
cases = product([1,2,3,4],repeat=len(cctvs))

min_cnt = float('inf')
for c in list(cases) : 
    cnt = 0
    tmp_board = copy.deepcopy(board)
    for i in range(len(c)) :
        set_dir(c[i],tmp_board,cctvs[i])

    for i in range(N) :
        for j in range(M) : 
            if tmp_board[i][j] == 0 : cnt += 1
    if cnt < min_cnt : 
        min_cnt = cnt

print(min_cnt)