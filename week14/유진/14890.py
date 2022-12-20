# 14890 : 경사로
import sys
input = sys.stdin.readline

N, L = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
slope = [[0]*N for _ in range(N)]

answer = 0 
for i in range(N):
    cnt = 1
    for j in range(N-1):
        next = board[i][j+1]
        if abs(board[i][j]-next) == 0 : 
            cnt += 1
        elif abs(board[i][j]-next) == 1 : 
            slope_check = False
            if next - board[i][j] > 0 : # 올라감
                if cnt >= L :
                    for k in range(L) : 
                        if not slope[i][j-k] : slope[i][j-k] = 1
                        else : 
                            slope_check = True
                            break
                else : break
            else : #내려감
                flag= False
                if j+L < N : 
                    for k in range(L):
                        if next != board[i][j+1+k] : 
                            flag= True
                            break
                        else : 
                            if not slope[i][j+1+k] : slope[i][j+1+k] = 1
                            else : 
                                slope_check = True
                                break
                else : break
                if flag : break
            cnt = 1
            if slope_check : break
        elif abs(board[i][j]-next) > 1 : break
        if j == N-2 : 
            answer += 1
            # print("i",i)

slope = [[0]*N for _ in range(N)]
for j in range(N):
    cnt = 1
    for i in range(N-1):
        next = board[i+1][j]
        if abs(board[i][j]-next) == 0 : 
            cnt += 1
        elif abs(board[i][j]-next) == 1 : 
            slope_check = False
            if next - board[i][j] > 0 : # 올라감
                if cnt >= L :
                    for k in range(L) : 
                        if not slope[i-k][j] : slope[i-k][j] = 1
                        else : 
                            slope_check = True
                            break
                else : break
            else : #내려감
                flag= False
                if i+L < N : 
                    for k in range(L):
                        if next != board[i+1+k][j] : 
                            flag= True
                            break
                        else : 
                            if not slope[i+1+k][j] : slope[i+1+k][j] = 1
                            else : 
                                slope_check = True
                                break
                else : break
                if flag : break
            cnt = 1
            if slope_check : break
        elif abs(board[i][j]-next) > 1 : break
        if i == N-2 : 
            answer += 1
            # print("j",j)

print(answer)