from collections import deque
N = int(input())
K = int(input())
app_pos = [list(map(int,input().split())) for _ in range(K)]
app_pos = [[i-1,j-1] for i,j in app_pos]
L = int(input())
moves_oper = [list(map(str, input().split())) for _ in range(L)]
moves_oper = [[int(i),str(v)] for i,v in moves_oper]

#R D L U
move_list = [(1,0),(0,1),(-1,0),(0,-1)]

def init():
    global N
    board = [[0]*N for _ in range(N)]
    snake = deque()
    snake.append([0,0])

    return board,snake

# 헤드, 현재 방향
def move(board, snake, c_d):
    # print("snake : ",snake)
    global app_pos, move_list
    finish_flag = False

    # snake head만 움직여줌
    snake_head = snake[0]
    snake_head[0], snake_head[1] = snake[0][0] + move_list[c_d][0], snake[0][1] + move_list[c_d][1]
    # 보드 끝에 닿으면 finish
    if snake_head[0] >= len(board[0]) or snake_head[1] >= len(board) or snake_head[0] < 0 or snake_head[1] < 0:
        finish_flag = True
        return finish_flag, snake
    # 자기 몸에 닿으면 finish
    for i, sk in enumerate(snake):
        if i != 0 and snake_head[0] == sk:
            finish_flag = True
            return finish_flag, snake

    # 사과를 먹었을 때
    if snake_head[0] in app_pos:
        del app_pos[app_pos.index(snake_head[0])]
        # tail 생성
        snake.append(snake[0])
        for i in range(-2, -len(snake), -1):
            snake[i] = snake[i-1]
        snake[0] = snake_head
    else:
        # 꼬리 움직이기
        if len(snake) !=1:
            # 몸을 전체적으로 update
            for i in range(-1, -len(snake), -1):
                snake[i] = snake[i-1]
            snake[0] = snake_head
       
    return finish_flag, snake


def solution(moves_oper):
    global app_pos, move_list
    board, snake = init()
    cur_dir = 0
    time_cnt = 0

    while True:
        time_cnt += 1
        if moves_oper != [] and time_cnt == moves_oper[0][0]:
            if moves_oper[0][1] == 'D':
                if cur_dir == 3 : cur_dir = 0
                else: cur_dir = cur_dir+1
            else:
                if cur_dir == 0 : cur_dir = 3
                else : cur_dir = cur_dir-1
            del moves_oper[0]               

        finish_flag, snake = move(board, snake, cur_dir)
        if finish_flag == True:
            break
    print(time_cnt)


solution(moves_oper)