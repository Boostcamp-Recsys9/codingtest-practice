def solution(gems):
    target = len(set(gems))
    get = {}
    end = 0
    
    while len(get) != target :
        if gems[end] not in get.keys() : get[gems[end]] = 1
        else : get[gems[end]] += 1
        end += 1

    for start in range(len(gems)):
        if get[gems[start]] > 1 : 
            get[gems[start]] -= 1
            start +=1
        else : break
    
    answer = [start+1,end]
    return answer