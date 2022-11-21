from collections import deque

def range_check(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    return False

n=int(input())
apple_count = int(input())
snake_pos = deque()
snake_pos.append((0,0))
forward = 0
board = [[0]*n for _ in range(n)]
for i in range(apple_count):
    x,y = map(int,input().split())
    board[x-1][y-1] = 1
cmd_cnt = int(input())
command = []
command_check=0
# L: 왼쪽, D:오른쪽
for i in range(cmd_cnt):
    sec,cmd = input().split()
    command.append([int(sec),cmd])
dx = [0,1,0,-1]
dy = [1,0,-1,0]
answer = 1
while True:
    x,y=snake_pos.pop()
    snake_pos.append((x,y))
    move_x = x+dx[forward%4]
    move_y = y+dy[forward%4]
    if not range_check(move_x,move_y) or (move_x,move_y) in snake_pos:
        break
    if board[move_x][move_y] ==0:
        snake_pos.popleft()
    else:
        board[move_x][move_y]=0
    snake_pos.append((move_x,move_y))
    if command_check < len(command) and command[command_check][0] == answer:
        if command[command_check][1] == 'L':
            forward-=1
        else:
            forward +=1
        command_check+=1
    answer+=1
print(answer)
    
    
