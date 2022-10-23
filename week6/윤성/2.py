import re
from copy import deepcopy
from itertools import permutations

def cal(x,y,oper):
    if oper == '+':
        return x+y
    if oper == "-":
        return x-y
    if oper == "*":
        return x*y

def solution(expression):
    answer = 0
    temp = ['+','-','*']
    oper = []
    result = []
    array = list(map(int, re.split('[-|+|*]', expression)))
    for i in expression:
        if i in temp:
            oper.append(i)
    opercnt = list(set(oper))
    operlist = list(permutations(opercnt,len(opercnt)))
    for cnt in operlist:
        newarr = deepcopy(array)
        newoper = deepcopy(oper)
        for opers in cnt:
            index = 0
            while True:
                if index >= len(newoper):
                    break
                else:
                    if newoper[index] == opers:
                        newarr[index] = cal(newarr[index],newarr[index+1],opers)
                        newarr.pop(index+1)
                        newoper.pop(index)
                    else:
                        index+=1             
        result.append(max(newarr[0],-newarr[0]))
    return max(result)