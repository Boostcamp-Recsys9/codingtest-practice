import sys
from itertools import permutations

N = int(input())
A = list(map(int,sys.stdin.readline().split()))
opsNum = list(map(int,sys.stdin.readline().split()))


op = []
'''
for i in range(4) :
    for j in range(opsNum[i]) :
        op.append(i+1)
'''
op += list('+'*opsNum[0]) + list('-'*opsNum[1]) + list('*'*opsNum[2]) + list('/'*opsNum[3])
orders = list(set(permutations(op,N-1)))

results = []
for order in orders :
    result = A[0]
    for i in range(len(order)) :
        if order[i] == '+' : 
            result += A[i+1]
        elif order[i] == '-' :
            result -= A[i+1]
        elif order[i] == '*' :
            result *= A[i+1]
        elif order[i] == '/' :
            if result < 0 :
                result = (-1)*((-1)*result // A[i+1])
            else : 
                result //= A[i+1]
    results.append(result)

print(max(results), min(results))     