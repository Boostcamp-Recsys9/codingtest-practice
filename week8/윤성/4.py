def solution(stones, k):
    start = 0
    answer =0
    end = max(stones)
    n = len(stones)
    while start<=end:
        mid = (start+end) // 2
        count = 0
        total = 0
        for m in range(n):
            if stones[m]-mid <=0:
                count+=1
            else:
                if total < count:
                    total = count
                count = 0
        if total < count:
            total = count    
        if total >= k:
            end = mid-1
            answer = mid
        else:
            start = mid+1
    return answer