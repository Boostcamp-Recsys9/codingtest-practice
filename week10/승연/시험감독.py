N = int(input())
A = list(map(int, input().split()))
B,C = map(int,input().split())
def solution():
    tot = 0
    for i in A:
        i = i-B
        tot+=1

        if i <= 0:
            continue
        tot += i//C
        if i%C != 0:
            tot+=1
    print(tot)

solution()