import heapq
from copy import deepcopy

def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    distance = [INF] * (n+1)
    path = {i:[] for i in range(1,n+1)}
    for fare in fares:
        path[fare[0]].append((fare[1],fare[2]))
        path[fare[1]].append((fare[0],fare[2]))
    standard = dijkstra(s,path,distance)
    for i in range(1,n+1):
        distance = [INF] * (n+1)
        passway = dijkstra(i,path,distance)
        answer=min(answer,passway[a]+passway[b]+standard[i])
    return answer

def dijkstra(start,path,distance):
    q=[]
    distance[start] =0
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in path[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q,(distance[i[0]],i[0]))
    return distance