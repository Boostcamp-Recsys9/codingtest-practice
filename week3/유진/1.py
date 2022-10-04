# 2022 KAKAO BLIND RECRUITMENT > 신고 결과 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/92334

from collections import OrderedDict

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    id_dict = OrderedDict([(k,i) for i,k in enumerate(id_list)])
    report = list(set(report))   #중복제거
    reported = [0 for _ in range(len(id_list))]
    source = [[] for _ in range(len(id_list))]
    
    for r in report : 
        s, d = r.split()
        reported[id_dict[d]] += 1
        source[id_dict[d]].append(s)
    for i in range(len(reported)) : 
        if reported[i] >= k : 
            for s in source[i] : 
                answer[id_dict[s]] +=1  
    return answer