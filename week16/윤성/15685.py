def find_square(arr):
    ans=0
    for i in range(100):
        for j in range(100):
            if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
                ans += 1
    return ans

n = int(input())
dx = [1,0,-1,0]
dy = [0,-1,0,1]
array = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    array[x][y] = 1
    move = [d]
    for i in range(g):
        curve = []
        for j in range(len(move)):
            curve.append((move[-j - 1] + 1) % 4)
        move.extend(curve)     
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        array[nx][ny] = 1
        x, y = nx, ny
print(find_square(array))