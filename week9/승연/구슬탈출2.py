from collections import deque

n,m = map(int, input().split())
board = [list(input().split()) for i in range(n)]
dx, dy = (0,0,1,-1), (1,-1,0,0)
# rx,ry,bx,by 방문처리 - 한번에 움직이기 때문에 가능함
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
q = deque()


def init():
    global board
    #r,b의 위치 찾기
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i,j
            elif board[i][j] == "B":
                bx,by = i,j

    q.append((rx,ry,bx,by),0)
    check[rx][ry][bx][by] = True


def move(x,y,dx,dy, c):
    global board
    while board[x+dx][y+dy] != '#' and board[x][y] =='O':
        x += dx
        y += dy
        c += 1
    return x,y,c


def bfs():
    while q:
        rx,ry,bx,by, c = q.popleft()
        if c>=10:  
            break
        for i in range(4):
            nrx,nry,rc = move(rx,ry,dx[i],dy[i], c)
            nbx,nby,bc = move(bx,by,dx[i],dy[i], c)
            if board[nbx][nby] != 'O':  
                if board[nrx][nry] == 'O':  
                    print(c)
                    return
                if nrx == nbx and nry == nby:  
                    if rc > bc:  
                        nrx -= dx[i]  
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                
                if not check[nrx][nry][nbx][nby]:
                    check[nrx][nry][nbx][nby] = True
                    
                    q.append((nrx, nry, nbx, nby, c+1))            

    print(-1)

init()