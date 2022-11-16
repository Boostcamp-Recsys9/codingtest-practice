from collections import deque

def bfs(red_x,red_y,blue_x,blue_y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue=deque()
    queue.append((1,red_x,red_y,blue_x,blue_y))
    while queue:
        cnt,red_x,red_y,blue_x,blue_y = queue.popleft()
        for i in range(4):
            red_nx,red_ny = red_x,red_y
            blue_nx,blue_ny=blue_x,blue_y
            while array[blue_nx+dx[i]][blue_ny+dy[i]] == '.':
                blue_nx += dx[i]
                blue_ny += dy[i]
            if array[blue_nx+dx[i]][blue_ny+dy[i]]=='O':
                continue

            while array[red_nx+dx[i]][red_ny+dy[i]]=='.':
                red_nx += dx[i]
                red_ny += dy[i]
            if array[red_nx+dx[i]][red_ny+dy[i]]=='O':
                return cnt
            else:
                if red_nx==blue_nx and red_ny==blue_ny:
                    if abs(red_x-red_nx) + abs(red_y-red_ny) > abs(blue_x-blue_nx)+abs(blue_y-blue_ny):
                        red_nx = red_nx-dx[i]
                        red_ny = red_ny-dy[i]
                    else:
                        blue_nx = blue_nx-dx[i]
                        blue_ny = blue_ny-dy[i]
                if [red_nx,red_ny,blue_nx,blue_ny] not in visited:
                    queue.append((cnt+1,red_nx,red_ny,blue_nx,blue_ny))
                    visited.append([red_nx,red_ny,blue_nx,blue_ny])
        if cnt>10:
            return -1
    return -1
        

n,m = map(int,input().split())
array = []
index = [0,1]
red_pos = [0,0]
blue_pos = [0,0]
for i in range(n):
    array.append(list(input()))
    for k in range(m):
        if array[i][k] == 'B':
            blue_pos = [i,k]
        elif array[i][k] == 'R':
            red_pos=[i,k]
array[red_pos[0]][red_pos[1]]='.'
array[blue_pos[0]][blue_pos[1]]='.'
visited = [[red_pos[0],red_pos[1],blue_pos[0],blue_pos[1]]]
print(bfs(red_pos[0],red_pos[1],blue_pos[0],blue_pos[1]))
