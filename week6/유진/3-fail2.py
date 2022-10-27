def solution(gems):
    target = len(set(gems))
    get = {}
    start, end = 0,0
    n = len(gems)
    min_len = float('inf')
    
    while start<n and end<n : 
        while len(get) != target :
            if gems[end] not in get.keys() : get[gems[end]] = 1
            else : get[gems[end]] += 1
            end += 1
        
        if get[gems[start]] > 1 : 
            get[gems[start]] -= 1
            start += 1
        else : 
            if end-start < min_len : answer = [start+1,end]
            del get[gems[start]]
            start = end
            get = {}

    return answer

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])