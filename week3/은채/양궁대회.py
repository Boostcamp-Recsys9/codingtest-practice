from itertools import combinations_with_replacement
def solution(n, info):
    ans = -1
    mryan = -1

    for cwr in combinations_with_replacement([c for c in range(0,11)], n):
        #print(cwr, end = '')
        apeach = 0
        ryan = 0
        for i in range(1, 11):
            if info[-i-1] < cwr.count(i):
                ryan += i
            else:
                if info[-i-1]>0:
                    apeach += i
        

        if (ryan > apeach) & (i==10) & (ryan-apeach > mryan):
            ans = cwr
            #print(cwr,end = "")
            mryan = ryan-apeach

    print(ans)
    answer = []
    if ans == -1:
        return [-1]
    
    for j in range(10,-1,-1):
        answer.append(ans.count(j))
    
    return answer
