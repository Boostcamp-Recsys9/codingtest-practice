from copy import deepcopy

def solution(info, edges):
    global answer,graph,state
    answer=0
    graph = {i:[] for i in range(len(info))}
    state = info
    visit = [0]*len(info)
    for start,end in edges:
        graph[start].append(end)
    dfs(0,0,0,visit,[])
    return answer

def dfs(node,sheep,wolf,visit,go_list):
    global answer,graph,state
    visit[node]=1
    print(node)
    go_list += graph[node]
    if state[node]:
        wolf+=1
    else:
        sheep+=1
    if sheep<=wolf:
        return False
    answer = max(answer,sheep)
    for go in go_list:
        go_next=[]
        for temp in go_list:
            if temp != go and not visit[temp]:
                go_next.append(temp)
        dfs(go,sheep,wolf,deepcopy(visit),go_next)