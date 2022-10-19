def solution(n, k, cmd):
    answer = ''
    row = {}
    stack = []
    for i in range(n):
        row[i]=0
    
    c_idx = k
    for i in cmd:
        if len(i) > 2:
            op, num = i.split()
            num = int(num)
            tmp = 0
            if op == 'D':
                for j in range(c_idx, c_idx+num):
                    if row[j]==1:
                        tmp+=1
                c_idx+=(num+tmp)
            else:
                for j in range(c_idx-num, c_idx):
                    if row[j]==1:
                        tmp+=1
                c_idx-=(num+tmp)
        else:
            op = i
            if op == "C":
                row[c_idx] = 1
                stack.append(c_idx)
                n -= 1
                if c_idx == n:
                    c_idx -= 1
                else:
                    c_idx += 1
            else:
                n+=1
                pop = stack.pop()
                row[pop] = 0

    for r in row.values():
        if r == 1:
            answer+='X'
        else:
            answer+='O'
    return answer




# n = 8
# k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# result = "OOOOXOOO"

# n = 8
# k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
# result = "OOXOXOOO"

n = 12
k = 4
cmd = ["D 2", 'C', 'D 1', 'C', 'U 4', "C", "Z", "C", "C", "C"]
# result = "OOXOXOOO"

print(solution(n, k, cmd))