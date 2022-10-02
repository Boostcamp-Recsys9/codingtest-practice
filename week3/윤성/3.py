def solution(fees, records):
    current_state={}
    last = 1439
    total={}
    for commend in records:
        time,number,state=commend.split(" ")
        current_state[number]=current_state.get(number,[])+[timechange(time)]
    for number,report in current_state.items():
        total_time=0
        report_num = len(report)
        if report_num %2==0:
            for i in range(0,report_num,2):
                total_time+=report[i+1]-report[i]
        else:
            for i in range(0,report_num-1,2):
                total_time+=report[i+1]-report[i]
            total_time+=last-report[-1]
        total[number]=calculate(total_time,fees)
    answer = [k[1] for k in sorted(total.items())]
    return answer

def timechange(time):
    hour,minute=map(int,time.split(":"))
    time_stack = hour*60+minute
    return time_stack

def calculate(times,fees):
    base_time,base_rate,sub_time,sub_charge = fees
    temp = max(times-base_time,0)
    per_charge=0
    if temp % sub_time==0:
        per_charge=temp//sub_time
    else:
        per_charge=temp//sub_time + 1
    result = base_rate + (per_charge * sub_charge)
    return result