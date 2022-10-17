from collections import deque

def dfs(person,array,x,y,cnt):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    queue.append((x,y,cnt))
    flag = 1
    while queue:
        if flag == 0:
            break
        x,y,cnt = queue.popleft()
        if cnt >= 2:
            pass
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or nx>=5 or ny<0 or ny>=5:
                    continue
                if array[nx][ny] == "X":
                    continue
                if array[nx][ny] == "P":
                    flag = 0
                    continue
                if array[nx][ny] == "O":
                    array[x][y] = "X"
                    queue.append((nx,ny,cnt+1))
    return flag

def solution(places):
    a = []
    for temp in places:
        array = []
        person = []
        result = 1
        for i in range(5):
            array.append(list(temp[i]))
            for k in range(5):
                if array[i][k] == 'P':
                    person.append((i,k,0))
        for i in person:
            if dfs(person,array,i[0],i[1],i[2]) == 0:
                result = 0
        a.append(result)
    return a