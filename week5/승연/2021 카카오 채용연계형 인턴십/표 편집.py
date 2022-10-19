def solution(n, k, cmd):
    answer = ''
    stack = []
    c_idx = k
    for i in cmd:
        if len(i) > 2:
            op, num = i.split()
            if op == "D":
                c_idx += int(num)
            elif op == "U":
                c_idx -= int(num)
        else:
            if i == 'C':
                stack.append(c_idx)
                if c_idx == n - 1:
                    c_idx -= 1
                else:
                    c_idx += 1
            elif i == "Z":
                stack.pop()

    for i in range(n):
        if not i in stack:
            answer += "O"
        else:
            answer +='X'

    return answer






n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
result = "OOOOXOOO"

# n = 8
# k = 2
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
# result = "OOXOXOOO"

print(solution(n, k, cmd))