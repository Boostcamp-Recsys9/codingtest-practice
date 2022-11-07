from itertools import permutations
import re
def F_operation(a,b,op):
    if op == '-':
        return str(int(a) -int(b))
    elif op == '*':
        return str(int(a) *int(b))
    elif op == '+':
        return str(int(a) +int(b))

def solution(expression):
    operation = [o for o in expression if not o.isdigit()]
    priority_operation = permutations(list(set(operation)))
    expression = list(re.findall(r'[0-9]+|[^0-9]', expression))
    max_num = []

    for prior_op in priority_operation:
        exp = expression.copy()
        for po in prior_op:
            flag = False
            idx = 0
            while len(exp) != 1:
                if exp[idx] == po and flag == False:
                    exp[idx-1] = F_operation(exp[idx-1], exp[idx+1], po)
                    del exp[idx+1], exp[idx]
                    if not po in exp:
                        flag = True
                    idx -=1
                if flag:
                    break
                idx+=1
        max_num.append(abs(int(exp[0])))

    answer = max(max_num)
    return answer


expression = "100-200*300-500+20"
# result = 60420

# expression = "50*6-3*2"
# result = 300

print(solution(expression))