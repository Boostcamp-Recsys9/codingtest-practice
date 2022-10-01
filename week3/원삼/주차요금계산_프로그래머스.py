import math
def solution(fees, records):
    # 차별 주치시간을 넣을 답 dict
    car_fee = {(i.split(' ')[1]):0 for i in records}
    # 현재 입차한 차들의 dict 
    in_car = {}
    # 진짜 답 리스트
    ans = []
    # 출차 없을시 최대 계산 시간
    max_time = [23,59]

    # 입차하는 차들에 대해서 in_car에 차번호:[입차 시, 입차 분] 형태로 넣어주기
    # 출차하는 차들에 대해서 in_car의 입차시 입차분과 출차시 출차분을 빼주고 분단위로 변환 뒤 car_fee에 더해주기(입차두번가능하기에)
    # 그리고 출차처리 되었으니 in_car에서 제거
    for i in records:
        if i.split(' ')[2] == 'IN':
            in_car[i.split(' ')[1]] = i.split(' ')[0].split(":")
        else:
            if i.split(' ')[1] in in_car:
                out_time = list(map(int,i.split(' ')[0].split(":")))
                in_time = list(map(int,in_car[i.split(' ')[1]]))
                time_ = [x-y for x,y in zip(out_time,in_time)]
                time = time_[0]*60 + time_[1]
                car_fee[i.split(' ')[1]] += time
                in_car.pop(i.split(' ')[1])

    # 그럼에도 출차처리가 안된 차들에 대해 최대출차시간을 적용시켜 위와 동일하게 분단위로 계산뒤 car_fee에 더해주기
    for i in in_car:
        out_time = max_time
        in_time = list(map(int,in_car[i]))
        time_ = [x-y for x,y in zip(out_time, in_time)]
        time = time_[0]*60 + time_[1]
        car_fee[i] += time

    # car_fee를 우선 번호순 sort후 fees정보에 맞춰서 요금 계산 ceil이용해서 올림하기 그리고 순서대로 ans에 넣기
    for i in sorted(car_fee.items(),key=lambda x:int(x[0])):
        if i[1] <= fees[0]:
            ans.append(fees[1])
        else:
            ans.append(math.ceil((i[1] - fees[0])/fees[2])*fees[3] + fees[1])
            
    return ans