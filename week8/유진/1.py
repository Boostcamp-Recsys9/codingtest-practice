# 코딩테스트 연습 > 2019 카카오 개발자 겨울 인턴십 > 튜플
# https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s= s.split('{')
    new_s = []
    for string in s : 
        if string : 
            string = string.rstrip(',')
            string = string.rstrip('}')
            new_s.append(list(map(int,string.split(','))))
    new_s.sort(key= lambda x:len(x))
    # print(new_s)
    answer = []
    for l in new_s : 
        for e in l :
            if e not in answer : answer.append(e)
    return answer