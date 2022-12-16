import sys
from itertools import combinations

N = int(input())
S = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
num = [i for i in range(N)]
combs = list(combinations(num,int(N/2)))
numset= set(num)

res = []
for c in combs :
    stat1, stat2 = 0,0
    start = list(combinations(c,2))
    link = list(combinations(list(numset - set(c)),2))
    for i,j in start : 
        stat1 += S[i][j]
        stat1 += S[j][i]
    for i,j in link : 
        stat2 += S[i][j]
        stat2 += S[j][i]
    res.append(abs(stat2-stat1))

print(min(res))