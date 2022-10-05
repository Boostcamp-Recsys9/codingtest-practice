def solution(fees, records):
    dic = {}
    for i in records:
        t, carnum, io = i.split()
        h, m = t.split(':')
        t = (int(h) * 60) + int(m)
        if io == 'IN':
            try:
                #print(carnum, dic[carnum])
                nt = - t - dic[carnum]
                dic[carnum] = nt
                #print(carnum, dic[carnum])
                
            except:
                dic[carnum] = -t
        else:
             dic[carnum] = t + dic[carnum]
    time = []    
    od = sorted(dic.items())
    print(od)
    for d in od:
        if d[1] <= 0:
            time.append(1439+d[1])
        else:
            time.append(d[1])
    print(time)
    print((23 * 60 + 59))
            
    answer = []
        
    return answer
