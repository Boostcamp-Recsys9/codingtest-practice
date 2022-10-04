# 결과의 평등에 미쳐버린 양궁대회;
# itertools의 product와 용법을 헛갈려서 처음부터 잘못 풀고 있었다...
from itertools import combinations_with_replacement as cwp
from collections import Counter
def solution(n, info):
    # cwp를 이용해서 중복포함되는 콤비네이션 리스트를 생성
    ryan_list = list(cwp(reversed(range(0,11)),n))
    # 최종 답이 될 점수차이와 라이언 점수리스트 생성
    final_score = -1
    final_info = [0] * 11

    # 각 만들어진 콤비네이션 리스트들에 대해서
    for x in ryan_list:
        ryan_info = [0] * 11
        ryan_score = 0
        apeach_score = 0
        # 점수별로 맞춘 수를 카운트해 info에 넣어주기 ~ 즉 인풋으로 받는 info와 동일한 형태가 되게
        for i in Counter(x).keys():
            ryan_info[i] = Counter(x)[i]
        ryan_info = list(reversed(ryan_info))
        # 인풋info와 라이언info 점수 비교해서 각각 점수 구하기
        for x,y in zip(range(0,11), reversed(range(0,11))):
            if info[x] < ryan_info[x]:
                ryan_score += y
            elif info[x] == 0 and ryan_info[x] == 0:
                pass
            else:
                apeach_score += y
        # 점수 차의 최대를 구하는 거니 점수 차로
        score_diff = ryan_score - apeach_score
        
        # 우선 라이언이 어피치보다 점수가 높고 이전 최고 점수차보다 이번 점수차가 크면 점수차와 info 갱신
        if ryan_score > apeach_score and score_diff > final_score:
            final_score = score_diff
            final_info = ryan_info
        # 만약 이전과 점수차가 같을 경우에는 뒤에서 부터 값을 각각 확인해서 0이 아니고 값이 더 큰 info를 가져가게
        elif ryan_score > apeach_score and score_diff == final_score:
            for x in reversed(range(0,11)):
                if ryan_info[x] > final_info[x]:
                    final_score = score_diff
                    final_info = ryan_info
                    break
                elif ryan_info[x] < final_info[x]:
                    break
                else:
                    pass
        else:
            pass
    
    # 만약 이러한 과정을 다 거쳤는데도 초기값과 같다면 -1 반환
    if final_info != [0] *11:
        return final_info
    else:
        return [-1]
                    
                
            