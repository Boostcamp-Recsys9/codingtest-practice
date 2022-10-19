def solution(places):
    answer = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    diag = [[1,1],[1,-1],[-1,1],[-1,-1]]

    for place in places:
      room_flag = True
      for ax_y, pla in enumerate(place):
        ax_x = list(pla)
        people_axis = [(ax_y, i) for i,v in enumerate(ax_x) if v == "P"]
        for y,x in people_axis:
          for move_x,move_y in zip(dx,dy):
            cx, cy = x + move_x, y + move_y

            if (cx < 0 or cx > 4 or cy<0 or cy > 4):
              continue

            if place[cy][cx] == "P":
              answer.append(0)
              room_flag = False
              break

            if place[cy][cx] == "O":
              for move_x,move_y in diag:
                cx, cy = x + move_x, y + move_y
                if (cx < 0 or cx > 4 or cy<0 or cy > 4):
                  continue

                if place[cy][cx] == "P":
                  answer.append(0)
                  room_flag = False
                  break
          
          if room_flag == False:
           break

        if room_flag == False:
          break
      if room_flag == True:
        answer.append(1)


    return answer

places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# result=[1, 0, 1, 1, 1]

print(solution(places))