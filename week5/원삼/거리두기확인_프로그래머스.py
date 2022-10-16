from itertools import combinations
def solution(places):
    # 각 사람이 앉은 경우를 확인해서 각각 자리의 combination사용
    ans = []
    for z in range(5):      
        person_list = []
        count = 0
        for y in range(5):
            for x in range(5):
                if places[z][x][y] == "P":
                    person_list.append([x,y])

        # 각자리간 거리 확인 후 거리두기가 안지켜지면 count + 1
        for i in combinations(person_list,2):
            x_len = abs(i[0][0]-i[1][0])
            y_len = abs(i[0][1]-i[1][1])
            # 각 자리 좌표의 최소 값 사용
            if x_len + y_len <= 1:
                count += 1
            elif x_len + y_len == 2:
                if x_len == 0:
                    m_ = min(i[0][1], i[1][1])
                    if places[z][i[0][0]][m_+1] == "O":
                        count += 1
                elif y_len == 0:
                    m_ = min(i[0][0], i[1][0])
                    if places[z][m_+1][i[0][1]] == "O":
                        count += 1                    
                else:
                    m_1 = min(i[0][0], i[1][0])
                    m_2 = min(i[0][1], i[1][1])
                    if places[z][i[0][0]][m_2+1] == "O" or places[z][m_1+1][i[0][1]] == "O" or places[z][m_1][m_2] == "O":
                        count += 1
            else:
                pass

            # 한자리라도 count되었으면 0 넣기
            if count > 0:
                ans.append(0)
                break
            else:
                pass
        # 최종적으로 모든 자리가 거리두기 count가 안되었다면 1 넣기
        if count == 0:
            ans.append(1)
                        
    return ans                   
                
                 