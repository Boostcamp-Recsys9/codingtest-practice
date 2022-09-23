from collections import deque
import heapq
INF=int(1e9)
def solution(n, paths, gates, summits):
    graph = {i:[] for i in range(1,n+1)}
    answer = []
    intensity = [INF] * (n+1)
    summits=set(summits)
    for i in paths:
        graph[i[0]] +=[(i[1],i[2])]
        graph[i[1]] +=[(i[0],i[2])]
    for j in gates:
        dijkstra(graph,j,intensity,summits)
    for summit in summits:
        answer.append((summit,intensity[summit]))
    answer.sort(key=lambda x:(x[1],x[0]))
    return answer[0]

def dijkstra(graph,start,intensity,summits):
    q=[]
    intensity[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,now=heapq.heappop(q)
        if now in summits or dist>intensity[now]:
            continue
        for i in graph[now]:
            cost = max(dist,i[1])
            if cost < intensity[i[0]]:
                intensity[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    