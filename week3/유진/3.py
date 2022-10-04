# 2022 KAKAO BLIND RECRUITMENT > 주차 요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math

def calc_time(in_time,out_time) : 
    in_h, in_m = map(int, in_time.split(':'))
    out_h, out_m = map(int, out_time.split(':'))
    time = (out_h - in_h)*60 + (out_m - in_m)
    return time

def solution(fees, records):
    answer = []
    IN, OUT, acc_times = {}, {}, {}
    costs = []
    
    for record in records : 
        t, key, typ = record.split()
        if typ == 'IN' : 
            if key in IN : 
                in_time = IN[key]
                out_time = OUT[key]
                if key in acc_times :acc_times[key] += calc_time(in_time, out_time) #⭐️
                else : acc_times[key] = calc_time(in_time, out_time)
                del OUT[key]
            IN[key] = t
        else : OUT[key] = t
    
    for key, in_time in IN.items() :
        if key in OUT : out_time = OUT[key]
        else : out_time = '23:59'
        acc_time = calc_time(in_time, out_time)
        if key in acc_times : acc_time += acc_times[key]
        if acc_time > fees[0] : cost = fees[1] + math.ceil((acc_time - fees[0])/fees[2]) * fees[3]
        else : cost = fees[1]
        costs.append((key,cost))

    costs.sort()
    for key,cost in costs :
        answer.append(cost)
    
    return answer