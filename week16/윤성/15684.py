# 새로 놓을 수 있는 사다리 구함
def possible(num):
    for combi in combinations(positions, num):
        if meet(combi):
            continue
        if linear_check(combi):
            return True
    return False


def meet(combi):
    for i, j in combi:
        if (1 <= j-1 and board[i][j-1]) or (j+1 <= n-1 and board[i][j+1]):
            return True
    return False

def go_x(j):
    y, x = 0, j
    while True:
        y += 1
        if y > h:
            break
        if board[y][x]:
            x += 1
        elif board[y][x-1]:
            x -= 1
    return x

def linear_check(combi):
    result = True
    for i, j in combi:
        board[i][j] = True
    for j in range(1, n+1):
        if j != go_x(j):
            result = False
            break
    for i, j in combi:
        board[i][j] = False
    return result

# init
from itertools import combinations
import sys
read = sys.stdin.readline
n, m, h = map(int, read().split())
board = [[0 for _ in range(n+1)] for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, read().split())
    board[a][b] = 1
positions = []
for i in range(h+1):
    for j in range(n):
        if not board[i][j]:
            positions.append((i, j))

# start
answer = -1
for num in range(4):
    if possible(num):
        answer = num
        break
print(answer)