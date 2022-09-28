# 코딩테스트 연습 > 2022 KAKAO TECH INTERNSHIP > 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666


def solution(survey, choices):
    answer = ''
    mbti_cnt = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    i = 0
    for s in survey : 
        if choices[i] < 4 : mbti_cnt[s[0]] += (4-choices[i])
        elif choices[i] > 4 : mbti_cnt[s[1]] += (choices[i]-4)
        i += 1

    if mbti_cnt['R'] < mbti_cnt['T'] : answer += 'T'
    else : answer += 'R'
    if mbti_cnt['C'] < mbti_cnt['F'] : answer += 'F'
    else : answer += 'C'
    if mbti_cnt['J'] < mbti_cnt['M'] : answer += 'M'
    else : answer += 'J'
    if mbti_cnt['A'] < mbti_cnt['N'] : answer += 'N'
    else : answer += 'A'

    return answer