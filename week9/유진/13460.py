# 구슬 탈출 2
import sys
import copy

def dfs(board, dir, R_loc, B_loc, cnt) :
    if cnt > max_move : return cnt

    rx, ry = R_loc
    bx, by = B_loc
    new_rx, new_ry = R_loc
    new_bx, new_by = B_loc
    hole = []
    
    if dir == 'up' :
        tmp_board = copy.deepcopy(board)
        first = None
        # R 이동
        tmp_board[rx][ry] = '.'
        for i in range(rx-1,-1,-1) :
            if tmp_board[i][ry] == '#' : break
            elif tmp_board[i][ry] == 'O' : 
                hole.append('R')
                break
            # elif tmp_board[i][ry] == '.' : new_rx -= 1
            # else : #B랑 경로가 겹치면
            #     new_rx -= 1
            #     first = 'B'
            else : new_rx -= 1

        tmp_board[bx][by] = '.'
        for i in range(bx-1,-1,-1) :
            if tmp_board[i][by] == '#' : break
            elif tmp_board[i][by] == 'O' : 
                hole.append('B')
                break
            # elif tmp_board[i][by] == '.' : new_bx -= 1
            # else : #R랑 경로가 겹치면
            #     new_bx -= 1
            #     first = 'R'
            else : new_bx -= 1
        
        if hole :
            if 'B' in hole : return
            elif 'R' in hole : 
                success.append(cnt) 
                return

        # if first=='B' : new_rx += 1
        # elif first=='R' : new_bx += 1
        if new_rx==new_bx and new_ry==new_by : 
            if abs(rx-new_rx) > abs(bx-new_bx) : new_rx += 1
            else :  new_bx += 1
        tmp_board[new_rx][new_ry] = 'R'
        tmp_board[new_bx][new_by] = 'B'

        new_R_loc = (new_rx, new_ry)
        new_B_loc = (new_bx, new_by)
        # dfs(tmp_board,'up',new_R_loc,new_B_loc, cnt+1)
        dfs(tmp_board,'down',new_R_loc,new_B_loc,cnt+1)
        dfs(tmp_board,'left',new_R_loc,new_B_loc,cnt+1)
        dfs(tmp_board,'right',new_R_loc,new_B_loc,cnt+1)
    
    elif dir == 'down' : 
        tmp_board = copy.deepcopy(board)
        first = None
        tmp_board[rx][ry] = '.'
        for i in range(rx+1,N) :
            if tmp_board[i][ry] == '#' : break
            elif tmp_board[i][ry] == 'O' : 
                hole.append('R')
                break
            # elif tmp_board[i][ry] == '.' : new_rx += 1
            # else : #B랑 경로가 겹치면
            #     new_rx += 1
            #     first = 'B'
            else : new_rx += 1 

        tmp_board[bx][by] = '.'
        for i in range(bx+1,N) :
            if tmp_board[i][by] == '#' : break
            elif tmp_board[i][by] == 'O' : 
                hole.append('B')
                break
            # elif tmp_board[i][by] == '.' : new_bx += 1
            # else : #R랑 경로가 겹치면
            #     new_bx += 1
            #     first = 'R'
            else : new_bx += 1

        if hole :
            if 'B' in hole : return
            elif 'R' in hole : 
                success.append(cnt) 
                return
    
        # if first=='B' : new_rx -= 1
        # elif first=='R' : new_bx -= 1
        if new_rx==new_bx and new_ry==new_by : 
            if abs(rx-new_rx) > abs(bx-new_bx) : new_rx -= 1
            else :  new_bx -= 1
        tmp_board[new_rx][new_ry] = 'R'
        tmp_board[new_bx][new_by] = 'B'
                
        new_R_loc = (new_rx, new_ry)
        new_B_loc = (new_bx, new_by)
        dfs(tmp_board,'up',new_R_loc,new_B_loc, cnt+1)
        # dfs(tmp_board,'down',new_R_loc,new_B_loc,cnt+1)
        dfs(tmp_board,'left',new_R_loc,new_B_loc,cnt+1)
        dfs(tmp_board,'right',new_R_loc,new_B_loc,cnt+1)
    
    elif dir == 'right' : 
        tmp_board = copy.deepcopy(board)
        first = None
        tmp_board[rx][ry] = '.'
        for j in range(ry+1,M) :
            if tmp_board[rx][j] == '#' : break
            elif tmp_board[rx][j] == 'O' : 
                hole.append('R')
                break
            # elif tmp_board[rx][j] == '.' : new_ry += 1
            # else : #B랑 경로가 겹치면
            #     new_ry += 1
            #     first = 'B'
            else : new_ry += 1
        
        tmp_board[bx][by] = '.'
        for j in range(by+1,M) :
            if tmp_board[bx][j] == '#' : break
            elif tmp_board[bx][j] == 'O' : 
                hole.append('B')
                break
            # elif tmp_board[bx][j] == '.' : new_by += 1
            # else : #R랑 경로가 겹치면
            #     new_by += 1
            #     first = 'R'
            else : new_by += 1 

        if hole :
            if 'B' in hole : return
            elif 'R' in hole : 
                success.append(cnt) 
                return

        # if first=='B' : new_ry -= 1
        # elif first=='R' : new_by -= 1
        if new_rx==new_bx and new_ry==new_by : 
            if abs(ry-new_ry) > abs(by-new_by) : new_ry -= 1
            else :  new_by -= 1
        tmp_board[new_rx][new_ry] = 'R'
        tmp_board[new_bx][new_by] = 'B'
                
        new_R_loc = (new_rx, new_ry)
        new_B_loc = (new_bx, new_by)
        dfs(tmp_board,'up',new_R_loc,new_B_loc, cnt+1)
        dfs(tmp_board,'down',new_R_loc,new_B_loc,cnt+1)
        dfs(tmp_board,'left',new_R_loc,new_B_loc,cnt+1)
        # dfs(tmp_board,'right',new_R_loc,new_B_loc,cnt+1)
    
    
    elif dir == 'left' : 
        tmp_board = copy.deepcopy(board)
        first = None
        tmp_board[rx][ry] = '.'
        for j in range(ry-1,-1,-1) :
            if tmp_board[rx][j] == '#' : break
            elif tmp_board[rx][j] == 'O' : 
                hole.append('R')
                break
            # elif tmp_board[rx][j] == '.' : new_ry -= 1
            # else : #B랑 경로가 겹치면
            #     new_ry -= 1
            #     first = 'B'
            else : new_ry -= 1


        tmp_board[bx][by] = '.'
        for j in range(by-1,-1,-1) :
            if tmp_board[bx][j] == '#' : break
            elif tmp_board[bx][j] == 'O' : 
                hole.append('B')
                break
            # elif tmp_board[bx][j] == '.' : new_by -= 1
            # else : #R랑 경로가 겹치면
            #     new_by -= 1
            #     first = 'R'
            else : new_by -= 1

        if hole :
            if 'B' in hole : return
            elif 'R' in hole : 
                success.append(cnt) 
                return

        # if first=='B' : new_ry += 1
        # elif first=='R' : new_by += 1
        if new_rx==new_bx and new_ry==new_by : 
            if abs(ry-new_ry) > abs(by-new_by) : new_ry += 1
            else :  new_by += 1
        tmp_board[new_rx][new_ry] = 'R'        
        tmp_board[new_bx][new_by] = 'B'

        new_R_loc = (new_rx, new_ry)
        new_B_loc = (new_bx, new_by)
        dfs(tmp_board,'up',new_R_loc,new_B_loc, cnt+1)
        dfs(tmp_board,'down',new_R_loc,new_B_loc,cnt+1)
        # dfs(tmp_board,'left',new_R_loc,new_B_loc,cnt+1)
        dfs(tmp_board,'right',new_R_loc,new_B_loc,cnt+1)

    return


N,M = map(int, input().split())
board = [list(sys.stdin.readline().rstrip('\n')) for _ in range(N)]
max_move = 10
success = []

for i in range(N) : 
    for j in range(M) : 
        if board[i][j] == 'R' :
            R_loc = (i,j)
        elif board[i][j] == 'B' : 
            B_loc = (i,j)

dfs(board,'up',R_loc,B_loc,1)
dfs(board,'down',R_loc,B_loc,1)
dfs(board,'right',R_loc,B_loc,1)
dfs(board,'left',R_loc,B_loc,1)

if len(success) == 0 : print(-1) 
else : print(min(success))