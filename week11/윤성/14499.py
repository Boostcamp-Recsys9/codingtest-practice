
def range_check(current_x,current_y,n,m):
    if 0<=current_x<n and 0<=current_y<m:
        return True
    return False

def rotate(dice,command):
    a,b,c,d,e,f = dice[1:]
    if command==1:
        dice=[0,c,b,f,a,e,d]
    elif command==2:
        dice=[0,d,b,a,f,e,c]
    elif command==3:
        dice=[0,b,f,c,d,a,e]
    else:
        dice=[0,e,a,c,d,f,b]
    return dice
            
def move(dice,current,command):
    if range_check(current[0]+dx[command-1],current[1]+dy[command-1],n,m):
        current[0] += dx[command-1]
        current[1] +=dy[command-1]
        dice = rotate(dice,command)
        if array[current[0]][current[1]] == 0:
            array[current[0]][current[1]] = dice[1]
        else:
            dice[1] = array[current[0]][current[1]]
            array[current[0]][current[1]] = 0
        print(dice[6])
        return dice,current
    else:
        return dice,current

dx = [0,0,-1,1]
dy = [1,-1,0,0] 
# 동->서->북->남
n,m,start_x,start_y,command = list(map(int,input().split()))
array = []
current = [start_x,start_y]
dice = [0] * 7
for i in range(n):
    array.append(list(map(int,input().split())))
command_list = list(map(int,input().split()))
for command in command_list:
    dice,current = move(dice,current,command)