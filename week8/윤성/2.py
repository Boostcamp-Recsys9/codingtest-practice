import re

def solution(s):
    answer = []
    table = {}
    new = re.split('[{|}|,]',s)
    for i in new:
        if i == "":
            pass
        else:   
            table[int(i)] = table.get(int(i),0)+1
    temp = sorted(table.items(),key=lambda x:-x[1])
    answer = [k[0] for k in temp]
    return answer