from itertools import combinations
def solution(places):
    # 답 리스트
    ans = []
    # 총 다섯개 시험장
    for z in range(5):
        # 사람이 앉은 상황에 대한 combination 리스트
        person_list = []
        # try
        count = 0
        # 각각 사람이 앉은 경우 확인 후 각 경우에 대해 좌표값을 combination
        for y in range(5):
            for x in range(5):
                if places[z][x][y] == "P":
                    person_list.append([x,y])

        # 각 좌표값에 대해 거리 구하기 ~ 1이하면 count +1 , 2일 경우 조건에 따라 지정, 이상이면 pass
        for i in combinations(person_list,2):
            x_len = abs(i[0][0]-i[1][0])
            y_len = abs(i[0][1]-i[1][1])
            if x_len + y_len <= 1:
                count += 1
            # 각 두 좌표값의 최소값을 이용해서 파티션이 없는 경우 확인
            elif x_len + y_len == 2:
                # P-P 모양으로 앉앗을 경우
                if x_len == 0:
                    m_ = min(i[0][1], i[1][1])
                    if places[z][i[0][0]][m_+1] == "O":
                        count += 1
                # | 모양으로  앉앗을 경우
                elif y_len == 0:
                    m_ = min(i[0][0], i[1][0])
                    if places[z][m_+1][i[0][1]] == "O":
                        count += 1            
                # 2*2로 앉앗을 경우        
                else:
                    m_1 = min(i[0][0], i[1][0])
                    m_2 = min(i[0][1], i[1][1])
                    if places[z][i[0][0]][m_2+1] == "O" or places[z][m_1+1][i[0][1]] == "O" or places[z][m_1][m_2] == "O":
                        count += 1
            else:
                pass
            # 하나의 앉은 경우에 대해 하나라도안지켯으면 break후 0전달
            if count > 0:
                ans.append(0)
                break
            else:
                pass
        # range z 내에서 한번도 0이 나올건이 없엇다면 1 
        if count == 0:
            ans.append(1)
                        
    return ans                   
                
                    
                    