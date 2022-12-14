dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m=map(int,input().split())
x,y,dir = list(map(int,input().split()))
array = []
answer=1
stop=False
for i in range(n):
    array.append(list(map(int,input().split())))
array[x][y] = 2
while True:
    flag = 0
    if stop:
        break
    for i in range(4):
        dir-=1
        nx=x+dx[dir%4]
        ny=y+dy[dir%4]
        if array[nx][ny] == 0:
            array[nx][ny] = 2
            answer+=1
            flag =1
            x,y=nx,ny
            break
    if flag==0:
        nx = x+dx[(dir-2)%4]
        ny = y+dy[(dir-2)%4]
        if array[nx][ny]==1:
            stop=True
        else:
            x,y=nx,ny
print(answer)