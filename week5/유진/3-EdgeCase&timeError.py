# 코딩테스트 연습 > 2021 카카오 채용연계형 인턴십 > 표 편집
# https://school.programmers.co.kr/learn/courses/30/lessons/81303

# 채점 결과
# 정확성: 28.0
# 효율성: 35.0
# 합계: 63.0 / 100.0

def solution(n, k, cmd):
    answer = ['O']*n
    delete_latest = []
    
    for i in range(len(cmd)) : 
        # print(k, answer)
        # print(delete_latest)
        if len(cmd[i]) > 1 :
            d, n_move = cmd[i].split() 
            if d == 'D' : 
                for j in range(int(n_move)) : 
                    k += 1
                    while (answer[k] != 'O') : k += 1
            elif d == 'U' : 
                for j in range(int(n_move)) :
                    k -= 1
                    while (answer[k] != 'O') : k -= 1
        else : 
            if cmd[i] == 'C' : 
                answer[k] = 'X'
                delete_latest.append(k)
                if k == n-1 : 
                    for j in range(1) :
                        k -= 1
                        while (answer[k] != 'O') : k -= 1
                else :
                    for j in range(1) : 
                        k += 1
                        while (answer[k] != 'O') : k += 1
            elif cmd[i] == 'Z' :
                answer[delete_latest[-1]] = 'O'
                delete_latest.pop()
    
    return ''.join(answer)