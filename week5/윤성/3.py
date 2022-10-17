def solution(n, k, cmd):
    cur = k
    table = {i:[i-1,i+1] for i in range(n)}
    table[0] = [None,1]
    table[n-1] = [n-2,None]
    answer = ['O'] * n
    stack = []
    for commend in cmd:
        if commend == 'C':
            prev,next = table[cur]
            answer[cur] = 'X'
            stack.append([prev,cur,next])
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]
            if prev == None:
                table[next][0] = prev
            elif next == None:
                table[prev][1] = next
            else:
                table[next][0] = prev
                table[prev][1] = next
        elif commend == 'Z':
            prev,now,next = stack.pop()
            answer[now] = 'O'
            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now
        else:
            commend = commend.split(" ")
            cnt = int(commend[1])
            if commend[0] == 'D':
                for i in range(cnt):
                    cur = table[cur][1]
            else:
                for i in range(cnt):
                    cur = table[cur][0]
    return (''.join(answer))