def solution(survey, choices):
    answer = ""
    score = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,'A':0,"N":0}
    for i in range(len(choices)):
        if choices[i] == 4:
            pass
        elif choices[i] == 1:
            score[survey[i][0]] += 3
        elif choices[i] == 2:
            score[survey[i][0]] += 2
        elif choices[i] == 3:
            score[survey[i][0]] += 1
        elif choices[i] == 5:
            score[survey[i][1]] += 1
        elif choices[i] == 6:
            score[survey[i][1]] += 2
        elif choices[i] == 7:
            score[survey[i][1]] += 3    
        else:
            pass
        # 각 상반된 유형을 인덱스 reverse되게 해놓고 자동으로 들어가게 해도 될듯?
    #1
    if score["R"] > score["T"]:
        answer += "R"
    elif score["R"] < score["T"]:
        answer += "T"
    else:
        answer += "R"
    #2      
    if score["C"] > score["F"]:
        answer += "C"
    elif score["C"] < score["F"]:
        answer += "F"
    else:
        answer += "C"
    #3 
    if score["J"] > score["M"]:
        answer += "J"
    elif score["J"] < score["M"]:
        answer += "M"
    else:
        answer += "J"
    #4  
    if score["A"] > score["N"]:
        answer += "A"
    elif score["A"] < score["N"]:
        answer += "N"
    else:
        answer += "A"
        # 마찬가지로 상반된 유형의 인덱스를 대응되게해서 줄을 줄일 수도?
        # 그치만 귀찬
    return answer
        