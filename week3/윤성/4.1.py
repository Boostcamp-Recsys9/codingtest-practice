def solution(n, info):
    global answer, score
    answer = [-1]
    score = 0
    dfs(0,n,info,[0 for _ in range(11)])
    return answer

def dfs(idx,arrow,info,me):
    global answer,score
    if arrow<0:
        return False
    if idx > 10:
        diff = score_calculate(info,me)
        if diff<=0:
            return
        if diff > score:
            score = diff
            answer = [me[i] for i in range(11)]
            answer[10]+=arrow
        return True
    me[10-idx] = info[10-idx]+1
    dfs(idx+1,arrow-me[10-idx],info,me)
    me[10-idx]=0
    dfs(idx+1,arrow,info,me)

def score_calculate(info,cases):
    info_score=0
    cases_score=0
    for i in range(0,11):
        if info[i] < cases[i]:
            cases_score+=(10-i)
        elif info[i]> cases[i]:
            info_score+=(10-i)
        else:
            if cases[i] > 0:
                info_score+=(10-i)
    return cases_score-info_score