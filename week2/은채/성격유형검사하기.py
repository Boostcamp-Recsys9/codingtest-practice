def solution(survey, choices):
    result = ""

    for i in range(len(survey)):
        cho = choices[i]
        if cho <4:
            result += survey[i][0] * (4-cho)
        else:
            result += survey[i][1] * cho
        
    print(result)
    
    
    if result.count("T") > result.count("R"):
        answer = "T"
    else:
        answer = "R"
        
    if result.count("F") > result.count("C"):
        answer += "F"
    else:
        answer += "C"
    
    if result.count("M") > result.count("J"):
        answer += "M"
    else:
        answer += "J"
    
    if result.count("N") > result.count("A"):
        answer += "N"
    else:
        answer += "A"
    
    return answer
