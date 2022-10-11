def solution(play_time, adv_time, logs):
    answer = ''
    total_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    time_array = [0 for _ in range(total_time+1)]
    for time in logs:
        start,end = time.split('-')
        time_array[str_to_int(start)]+=1
        time_array[str_to_int(end)]-=1
    for i in range(1,len(time_array)):
        time_array[i] += time_array[i-1]
    for i in range(1,len(time_array)):
        time_array[i] += time_array[i-1]
    most_time=0
    max_view=time_array[adv_time-1]
    for time in range(adv_time,total_time):
        if max_view < time_array[time]-time_array[time-adv_time]:
            max_view = time_array[time]-time_array[time-adv_time]
            most_time = time-adv_time+1
    answer = int_to_str(most_time)
    return answer


def str_to_int(time):
    hour,minute,second=map(int,time.split(":"))
    return hour*3600+minute*60+second

def int_to_str(second):
	array = []
	hour = second // 3600
	second-=3600*hour
	array.append(str(hour))
	minute=second//60
	array.append(str(minute))
	second-=60*minute
	array.append(str(second))
	result =""
	for i in range(3):
		if len(array[i])==1:
			array[i] ='0'+ array[i]
		result += array[i]+':'
	return result[:-1]