from itertools import combinations

def team_cal(array,graph):
    result=0
    for i in range(len(array)-1):
        start=array[i]
        for j in range(i+1,len(array)):
            end=array[j]
            result+=(graph[start][end]+graph[end][start])
    return result

n=int(input())
team=[i for i in range(n)]
answer=[]
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
team_list = list((combinations(team,n//2)))
for content in team_list:
    start=list(content)
    link=list(set(team)-set(content))
    start_val=team_cal(start,graph)
    link_val=team_cal(link,graph)
    answer.append(abs(start_val-link_val))
print(min(answer))

