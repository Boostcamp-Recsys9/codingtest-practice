def solution(n, k):
    # 진수 변경한 값을 넣을 빈 문자열
    ans = ""
    # 반환할 답 값
    real_ans = 0
    # 진수로 변환후, split하느라 생긴 빈값들 제거
    while n != 0:
        ans += str(n%k)
        n = n//k
    else:
        ans = ans[::-1]
    ans = ans.split("0")
    ans = list(map(int,filter(None, ans)))
    
    # 비교적 많이 본 소수 찾기 ~ 1은 제외
    for i in ans:
        count = 0
        if i != 1:
            # i/2로 갈 범위 지정시 테케에서 시간초과가 남으로 제곱근으로 변경
            for k in range(2,int(i**0.5)+1):
                if i%k == 0:
                    count += 1
                    break
                else:
                    pass
            if count == 0:
                real_ans += 1
            else:
                pass
    return real_ans
                    
    
                
