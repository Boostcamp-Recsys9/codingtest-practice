from collections import deque

def solution(maps):
    now = deque() 
    now.append([0,0,1]) 
    move = [[1,0],[0,1],[-1,0],[0,-1]] 
    
    while len(now) != 0: 
        last_x,last_y,count = now.popleft() 
        maps[last_x][last_y] = 0 
        for i in move:
            go_x = last_x + i[0]
            go_y = last_y + i[1] 
            if go_x == len(maps)-1 and go_y == len(maps[0])-1: 
                count += 1 
                return count
            elif 0 <= go_x <= len(maps)-1 and 0<= go_y <= len(maps[0])-1 and maps[go_x][go_y]==1:
                count +=1 
                now.append([go_x,go_y,count]) 
    else:
        return -1