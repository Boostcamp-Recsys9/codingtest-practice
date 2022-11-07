from itertools import permutations
from copy import deepcopy


def solution(user_id, banned_id):
    answer = 0
    answer_list = []
    users = list(set(permutations(user_id,len(banned_id))))
    for user in users:
        ban = deepcopy(banned_id)
        for u in user:
            for b in ban:
                if compare_text(u,b):
                    ban.remove(b)
                    break
        if len(ban)==0:
            answer_list.append(sorted(user))
    answer_list = set(map(tuple,answer_list))
    answer = len(answer_list)
    return answer


def all_index(text):
    index = []
    for i in range(len(text)):
        if text[i]=="*":
            index.append(i)
    return index

def compare_text(text1,text2):
    if len(text1) == len(text2):
        index = all_index(text2)
        for i in index:
            text1 = text1[:i]+"*"+text1[i+1:]
        if text1 == text2:
            return True
    return False