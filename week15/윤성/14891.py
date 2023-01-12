from collections import deque

def rotation(chain:deque,dir:int):
    if dir == 1:
        forward = chain.pop()
        chain.appendleft(forward)
        return chain
    else:
        reverse = chain.popleft()
        chain.append(reverse)
        return chain

def rotation_check(chain_1, chain_2):
    if chain_1[2] == chain_2[6]:
        return False
    else:
        return True

# 2,6보고 회전할지 안할지 체크
chains = []
for i in range(4):
    chains.append(deque(list(map(int,input()))))
n = int(input())
command = []
for i in range(n):
    command.append(list(map(int,input().split())))
for pos,dir in command:
    check = []
    for i in range(3):
        check.append(rotation_check(chains[i],chains[i+1]))
    if pos == 1:
        chains[0] = rotation(chains[0],dir)
        dir = -dir
        for i in range(0,3):
            if check[i]:
                chains[i+1] = rotation(chains[i+1],dir)
                dir=-dir
            else:
                break
    elif pos == 2:
        chains[1] = rotation(chains[1],dir)
        dir = -dir
        if check[0]:
            chains[0] = rotation(chains[0],dir)
        for i in range(1,3):
            if check[i]:
                chains[i+1] = rotation(chains[i+1],dir)
                dir=-dir
            else:
                break
    elif pos == 3:
        chains[2] = rotation(chains[2],dir)
        dir = -dir
        if check[2]:
            chains[3] = rotation(chains[3],dir)
        for i in range(1,-1,-1):
            if check[i]:
                chains[i] = rotation(chains[i],dir)
                dir=-dir
            else:
                break
    elif pos == 4:
        chains[3] = rotation(chains[3],dir)
        dir = -dir
        for i in range(2,-1,-1):
            if check[i]:
                chains[i] = rotation(chains[i],dir)
                dir=-dir
            else:
                break
answer = 0
weight = 1
for chain in chains:
    answer += weight*chain[0]
    weight *= 2
print(answer)