# 결과의 평등에 미쳐버린 양궁대회;
def solution(n, info):
    answer = []
    apeach_score = []
    ryan_info = [0] *11
    final_score = 0
    for i,x in zip(info, reversed(range(11))):
        try:
            apeach_score.append(x/i)
        except:
            apeach_score.append(0)
    for i,x in zip(range(len(ryan_info)),reversed(range(11))):
        win_point = info[i] + 1
        ryan_score = x/win_point
        if ryan_score >= apeach_score[i] and win_point <= n:
            ryan_info[i] = win_point
            n -= win_point
        elif ryan_score*2 == apeach_score[i] and info[i]==1 and win_point <= n:
            ryan_info[i] = win_point
            n -= win_point
        else:
            pass
    if n>0:
        ryan_info[-1] = n
        
    for x,y,z in zip(ryan_info, info, reversed(range(11))):
        if x>y:
            final_score += z
        elif x<y:
            final_score -= z
        else:
            pass
    
    if final_score > 0:
        return ryan_info
    else:
        return [-1]