# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):
    answer = 0
    stack = []
    for n in moves : 
        n -= 1 
        for i in range(len(board)) :
            if board[i][n] == 0 : continue
            if stack and stack[-1] == board[i][n] : 
                stack.pop()
                answer += 2
            else : stack.append(board[i][n])
            board[i][n] = 0
            break
    return answer