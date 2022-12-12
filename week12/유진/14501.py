import sys
# sys.setrecursionlimit(10**6)

N = int(input())
T,P = [],[]
for i in range(N) : 
  t,p = map(int,sys.stdin.readline().split())
  T.append(t)  
  P.append(p)
T.append(16)
P.append(0)

max = 0
def dfs (day, money) :
    global max
    if money > max : max = money
    #상담 o
    if day +T[day] < N+1 : dfs(day+T[day], money+P[day])
    #상담 X
    if day +1 < N+1 : dfs(day+1, money)

dfs(0,0)
print(max)
