def solution(numbers, hand):
    lh = '*'
    rh = '#'
    answer = ''
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            lh = str(n)
        elif n in [3,6,9]:
            answer += 'R'
            rh = str(n)
        else:
            print(n, lh, rh)      
    return answer
