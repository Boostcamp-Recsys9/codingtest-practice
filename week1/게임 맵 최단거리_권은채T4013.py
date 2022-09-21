def solution(maps):
    # 캐릭터 위치, 방문 노드, 방향
    answer = 0
    locx = 0
    locy = 0
    visit = [[0]*len(maps[0])]*len(maps)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visit[locx, loxy] = 1
    
    while True:
        for i in range(4):
            gox = locx + dx
            goy = locy + dy
            if gox<0 or gox>len(map[0]):
                continue
            elif if goy<0 or goy>len(map):
                continue
            if map[gox,goy] !=1:
                continue
                
    return answer
