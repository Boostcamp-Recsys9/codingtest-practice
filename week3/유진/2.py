# 2022 KAKAO BLIND RECRUITMENT > k진수에서 소수 개수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

import math

def is_prime(x) : #⭐️
    if(x<2) : return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return False 
    return True 

def to_k(n,k) :
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)   #몫과 나머지를 return
        rev_base += str(mod)
    return rev_base[::-1] 

def solution(n, k):
    answer = 0
    k_num = to_k(n,k).split('0')
    for cand in k_num :
        if cand != '' and is_prime(int(cand)) : answer += 1
    return answer