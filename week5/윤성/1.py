def solution(s):
    answer = 0
    number = ['0','1','2','3','4','5','6','7','8','9']
    alp = ['zero','one','two','three','four','five','six','seven','eight','nine']
    count = 0
    temp = s[0]
    tmpans = ""
    while True:
        if temp in number:
            count +=1
            tmpans += temp
            if count == len(s):
                break
            temp = s[count]
        elif temp in alp:
            count += 1
            tmpans += number[alp.index(temp)]
            if count == len(s):
                break
            temp = s[count]
        else:
            count +=1
            if count == len(s):
                break
            temp += s[count]
    return int(tmpans)