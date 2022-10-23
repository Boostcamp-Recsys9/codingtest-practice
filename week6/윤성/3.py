def solution(gems):
    result = [0,0]
    n = len(gems)
    total = len(set(gems))
    start = 0
    end = 0
    index = len(gems)+1
    dic = {gems[0] : 1}
    while start<n and end <n:
        if len(dic) < total:
            end+=1
            if end == n:
                break
            dic[gems[end]] = dic.get(gems[end],0) + 1
        else:
            if (end-start-1) < index:
                index = end-start-1
                result = [start+1,end+1]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]]-=1
            start+=1
    return result