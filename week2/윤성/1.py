def solution(survey, choices):
    answer = ''
    pivot = ['RT','CF','JM','AN']
    case = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for k in range(len(choices)):
        if choices[k]<4:
            case[survey[k][0]]+=4-choices[k]
        else:
            case[survey[k][1]]+=choices[k]-4
    print(case)
    # RT,CF,JM,AN
    for k in pivot:
        if case[k[0]] >= case[k[1]]:
            answer+=k[0]
        else:
            answer+=k[1]
    return answer