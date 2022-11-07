import sys
sys.setrecursionlimit(10**4)
def find(room_table,x):
    if not room_table.get(x):
        room_table[x] = x + 1
        return x
    else:
        room_table[x] = find(room_table,room_table[x])
        return room_table[x]



def solution(k, room_number):
    result = []
    room_table = {}
    for room in room_number:
        result.append(find(room_table,room))
    return result