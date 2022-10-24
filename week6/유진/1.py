# 코딩테스트 연습 > 2020 카카오 인턴십 > 키패드 누르기
# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    lh_dist = {1:[1,2,3,4],4:[2,1,2,3],7:[3,2,1,2],'*':[4,3,2,1],2:[0,1,2,3],5:[1,0,1,2],8:[2,1,0,1],0:[3,2,1,0]}
    rh_dist = {3:[1,2,3,4],6:[2,1,2,3],9:[3,2,1,2],'#':[4,3,2,1],2:[0,1,2,3],5:[1,0,1,2],8:[2,1,0,1],0:[3,2,1,0]}
    lh = '*'
    rh = '#'
    answer = ''    
    for n in numbers : 
        if n in [1,4,7] : 
            answer += 'L'
            lh = n
        elif n in [3,6,9] : 
            answer += 'R'
            rh = n
        else : 
            if n==2 : k=0
            elif n==5 : k=1
            elif n==8 : k = 2
            elif n==0 : k = 3
            
            if lh_dist[lh][k] < rh_dist[rh][k] : 
                answer += 'L'
                lh = n
            elif lh_dist[lh][k] > rh_dist[rh][k] : 
                answer += 'R'
                rh = n
            else : 
                if hand == 'right' : 
                    answer += 'R'
                    rh = n
                else : 
                    answer += 'L'
                    lh = n
    return answer