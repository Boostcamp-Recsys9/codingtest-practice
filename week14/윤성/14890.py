def possible(array,n):
    pos=array[0]
    index=1
    count=1 # 경사로를 쌓을 수 있는지 확인하기 위한 변수
    while index<len(array):
        if pos == array[index]: # 같은 값 나올때
            count+=1
            index+=1
        elif pos+1 == array[index]: # 올라가는 경사 생길때
            if count >=n: # 경사로를 쌓을 수 있는 경우
                pos=array[index]
                count=1 # 초기화
                index+=1
            else:
                return 0
        elif pos-1==array[index]: # 내려가는 경사 생길때
            if index+n>len(array): # array index 벗어나는 경우
                return 0
            else:
                for i in range(index,index+n): # 필요한 경사로 칸 수만큼 pos-1값이 존재하는지 확인
                    if array[i] != pos-1:
                        return 0 # 없는 경우
            pos=array[index]
            index+=n
            count=0
        else: # 경사가 2이상으로 들어오는 경우
            return 0
    return 1
l,n=map(int,input().split())
array=[]
answer = []
for i in range(l):
    temp_array = list(map(int,input().split()))
    answer.append(possible(temp_array,n)) # 열 체크
    array.append(temp_array)
    
for i in range(l):
    row=[]
    for j in range(l):
        row.append(array[j][i])
    answer.append(possible(row,n)) # 행 체크
print(sum(answer))