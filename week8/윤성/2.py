import re

def solution(s):
    answer = []
    temp = []
    array = []
    d = [0] * 100001
    new = re.split('[{|}|,]',s)
    for i in new:
        if i == "":
            pass
        else:   
            d[int(i)]+=1
    for k in range(max(d),0,-1):
        answer.append(d.index(k))
    return answer