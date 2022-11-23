import sys

N = int(input())
board = [[0]*(N+2) for _ in range(N+2)]
snake = []
cnt = 0

for i in range(N+2) :
    for j in range(N+2) :
        if i == 0 or j == 0 or i==N+1 or j==N+1 :
            board[i][j] = -1
board[1][1] = -1
snake.append((1,1))

def go(snake,ddir) : 
    global cnt
    cnt += 1
    hx,hy = snake[-1]
    tx,ty = snake[0]
    dx,dy = ddir
    if board[hx+dx][hy+dy] == -1 : 
        print(cnt) 
        sys.exit(0)
    elif board[hx+dx][hy+dy] == 0 : #★
        board[tx][ty] = 0 
        del snake[0] 
    board[hx+dx][hy+dy] = -1
    snake.append((hx+dx,hy+dy))
        
K = int(input())
for i in range(K) :
    i, j = map(int,sys.stdin.readline().split())
    board[i][j] = 1

L = int(input())
dxdy = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0
xc = []
for i in range(L) :
    xc.append(input().split())

for X,C in xc :    
    for sec in range(int(X)-cnt) : 
        go(snake, dxdy[d%4]) #★
    if C == 'L' : d-=1
    elif C == 'D' : d+=1 
    
while(True) : go(snake, dxdy[d%4]) #★