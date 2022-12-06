n=int(input())
works=list()
for i in range(n):
    works.append(list(map(int,input().split())))
dp = [0] * (n+1)
for i in range(n):
    if i + works[i][0]-1 < n:
        dp[i+works[i][0]-1] = max(dp[i+works[i][0]-1],dp[i-1]+works[i][1])
    dp[i] = max(dp[i],dp[i-1])
print(dp[n-1])