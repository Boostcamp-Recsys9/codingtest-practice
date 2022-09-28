def solution(n, k):
    answer = 0
    code=change(n,k)
    number_list = code.split('0')
    for number in number_list:
        if len(number)>0:
            if check_prime(int(number)):
                answer+=1
    return answer

def change(n,k):
    temp = n
    numbers=[]
    while temp > 0:
        numbers.append(str(temp % k))
        temp = temp//k
    return "".join(numbers)[::-1]

def check_prime(n):
    if n==1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k==0:
            return False
    return True