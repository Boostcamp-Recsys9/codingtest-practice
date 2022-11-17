import sys
from itertools import product
import copy 

def return_maxresult(board,move):
    n = len(board)
    for m in move :
        if m == 'r': 
            for i in range(n):
                point = n-1 # (i,j)번째 원소가 비교할 곳?
                for j in range(n-1,-1,-1): 
                    if board[i][j] != 0 :
                        tmp = board[i][j] 
                        board[i][j] = 0

                        if board[i][point] == tmp :
                            board[i][point] *= 2
                            point -= 1  #한번 합쳐진 블록은 다시 합쳐질 수 없음 
                        elif board[i][point] == 0: 
                            board[i][point] = tmp
                        else : 
                            point -= 1
                            board[i][point] = tmp #바로 옆에 붙임
                    
        elif m == 'l':
            for i in range(n):
                point = 0
                for j in range(n):
                    if board[i][j] != 0 :
                        tmp = board[i][j]
                        board[i][j]= 0

                        if board[i][point] == tmp :
                            board[i][point] *= 2
                            point += 1  #한번 합쳐진 블록은 다시 합쳐질 수 없음 
                        elif board[i][point] == 0: 
                            board[i][point] = tmp
                        else : 
                            point +=1 
                            board[i][point] = tmp #바로 옆에 붙임
            
        elif m == 'u':
            for i in range(n):
                point = 0
                for j in range(n):
                    if board[j][i] != 0 :
                        tmp = board[j][i]
                        board[j][i]= 0

                        if board[point][i] == tmp :
                            board[point][i] *= 2
                            point += 1  #한번 합쳐진 블록은 다시 합쳐질 수 없음 
                        elif board[point][i] == 0: 
                            board[point][i] = tmp
                        else : 
                            point +=1
                            board[point][i] = tmp #바로 아래에 붙임
       
        elif m == 'd': 
            for i in range(n):
                point = n-1
                for j in range(n-1,-1,-1): 
                    if board[j][i] != 0 :
                        tmp = board[j][i] 
                        board[j][i] = 0

                        if board[point][i] == tmp :
                            board[point][i] *= 2
                            point -= 1  #한번 합쳐진 블록은 다시 합쳐질 수 없음 
                        elif board[point][i] == 0: 
                            board[point][i] = tmp
                        else : 
                            point -= 1
                            board[point][i] = tmp #바로 옆에 붙임

    return max(map(max,board))

N = int(input())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer = 0
max_move = 5
move_list = ['u','d','l','r']
move_permutations = list(product(move_list, repeat=max_move))

for move_lists in move_permutations: 
    tmp_board = copy.deepcopy(board)
    for move in move_lists :
        result = return_maxresult(tmp_board,move)
        if answer < result : answer = result

print(answer)