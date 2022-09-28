from collections import deque

def solution(rc, operations):
    r_len,c_len = len(rc),len(rc[0])
    answer = []
    row = deque(deque(row[1:-1]) for row in rc)
    out_col = [deque(rc[i][0] for i in range(r_len)),deque(rc[k][c_len-1] for k in range(r_len))]
    for commend in operations:
        if commend == "ShiftRow":
            row.appendleft(row.pop())
            out_col[0].appendleft(out_col[0].pop())
            out_col[1].appendleft(out_col[1].pop())
        else:
            row[r_len-1].append(out_col[1].pop())
            out_col[0].append(row[r_len-1].popleft())
            row[0].appendleft(out_col[0].popleft())
            out_col[1].appendleft(row[0].pop())
    for k in range(r_len):
        temp = []
        temp.append(out_col[0][k])
        temp.extend(row[k])
        temp.append(out_col[1][k])
        answer.append(temp)
    return answer