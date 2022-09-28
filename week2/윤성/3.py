def solution(alp, cop, problems):
    answer = 0
    alp_max=0
    cop_max=0
    n= len(problems)
    INF=int(1e9)
    for i in problems:
        alp_max=max(alp_max,i[0])
        cop_max=max(cop_max,i[1])
    dp = [[INF for _ in range(cop_max+1)] for _ in range(alp_max+1)]
    alp=min(alp_max,alp)
    cop=min(cop_max,cop)
    dp[alp][cop]=0
    for i in range(alp,alp_max+1):
        for j in range(cop,cop_max+1):
            if i+1<=alp_max:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j]+1)
            if j+1<=cop_max:
                dp[i][j+1] = min(dp[i][j+1],dp[i][j]+1)
            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i>=alp_req and j>=cop_req:
                    ret_alp = min(alp_max,i+alp_rwd)
                    ret_cop=min(cop_max,j+cop_rwd)
                    dp[ret_alp][ret_cop] = min(dp[ret_alp][ret_cop],dp[i][j]+cost)
    answer = dp[-1][-1]     
    return answer