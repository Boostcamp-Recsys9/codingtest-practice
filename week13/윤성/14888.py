from itertools import permutations

def calculate(front,back,oper):
    if oper=='+':
        return front+back
    elif oper=='-':
        return front-back
    elif oper=='*':
        return front*back
    elif oper=='/':
        return int(front/back)

answer = []
n=int(input())
numbers = list(map(int,input().split()))
oper_input = list(map(int,input().split()))
opers = []
cases = ['+','-','*','/']
for i in range(4):
    for k in range(oper_input[i]):
        opers.append(cases[i])
total = list(set(permutations(opers,n-1)))
for content in total:
    score = numbers[0]
    for i in range(0,n-1):
        score = calculate(score,numbers[i+1],content[i])
    answer.append(score)
print(max(answer))
print(min(answer))