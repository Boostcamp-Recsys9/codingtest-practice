def is_prime(n):
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    tmp = ''
    while n >0:
        tmp += str(n % k)
        n = n // k
    temp = tmp[::-1]
    l = temp.split('0')

    answer = 0
    for i in l:
        if i != '':
            if int(i) >= 2:
                if is_prime(int(i)) == True:
                    print(i)
                    answer +=1

    return answer
