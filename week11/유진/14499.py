# 주사위 굴리기
import sys

input = sys.stdin.readline
N, M, x, y, K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
move_dir = list(map(int,input().split())) 
dice = [0,0,0,0,0,0]
'''
  2
4 1 3
  5
  6
'''
def roll(dir, dice):
    if dir == 1: dice = [dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    elif dir == 2: dice = [dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    elif dir == 3: dice = [dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
    elif dir == 4: dice = [dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    return dice

nx, ny = x, y
for i in move_dir : 
    if i==1: #동
        if 0 <= ny+1 < M: 
            ny += 1
            dice = roll(i, dice)
        else : continue
    elif i==2: #서
        if 0 <= ny-1 < M: 
            ny -= 1 
            dice = roll(i, dice)
        else : continue
    elif i==3: #북
        if 0 <= nx-1 < N: 
            nx -= 1
            dice = roll(i, dice)
        else : continue
    elif i==4: #남
        if 0 <= nx+1 < N: 
            nx += 1
            dice = roll(i, dice)
        else : continue

    # top = dice[5]
    # bottom = dice[0]
    if board[nx][ny]:
        dice[0] = board[nx][ny]
        board[nx][ny] = 0
    else: 
        board[nx][ny] = dice[0]
    print(dice[5])

