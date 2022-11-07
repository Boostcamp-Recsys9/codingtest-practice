def solution(k, room_number):
    table = {}
    answer = []
    for i in room_number:
        if table.get(i) == None:
            table[i] = i+1
            answer.append(i)
        else:
            k = table[i]
            temp =[k]
            while True:
                if table.get(k) == None:
                    for l in temp:
                        table[l] = k+1
                    table[k] = k+1
                    answer.append(k)
                    break
                else:
                    k = table[k]
                    temp.append(k)
    return answer