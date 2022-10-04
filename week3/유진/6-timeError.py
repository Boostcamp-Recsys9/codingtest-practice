# 2022 KAKAO BLIND RECRUITMENT > 파괴되지 않은 건물
# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
    answer = 0
    for s in skill :
        if s[0] == 1 : 
            for i in range(s[1],s[3]+1) : 
                for j in range(s[2],s[4]+1) :
                    board[i][j] -= s[5]
        else : 
            for i in range(s[1],s[3]+1) : 
                for j in range(s[2],s[4]+1) :
                    board[i][j] += s[5]

    for i in range(len(board)) : 
        for j in range(len(board[0])) :
            if board[i][j] > 0 : answer += 1
    
    return answer