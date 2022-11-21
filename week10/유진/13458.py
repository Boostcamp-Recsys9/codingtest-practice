import sys
import math

N = int(input())
students = list(map(int,sys.stdin.readline().split()))
cap_main , cap_assist = map(int,sys.stdin.readline().split())

cnt = 0
for snum in students :
    if snum - cap_main <= 0 : cnt += 1
    else : cnt += math.ceil((snum - cap_main) / cap_assist) + 1
print(cnt)