def init(gems):
    x1, x2 = 0, 0
    have_gem = [gems[x1]]
    have_gem2 = []

    return x1, x2, have_gem, have_gem2

def solution(gems):
    answer = []
    len_unique_gems = len(list(set(gems)))
    x1, x2, have_gem, have_gem2 = init(gems)

    min_len_list = []
    idx = 0
    len_gems = len(gems)
    min_len = 10000

    while not idx == len_gems:
        x2 += 1
        if not gems[x2] in have_gem:
            have_gem.append(gems[x2])
        if len(have_gem) == len_unique_gems:
            have_gem2.append(gems[x2])
            x1 = x2
            while len(have_gem2) != len_unique_gems:
                x1 -= 1
                if not gems[x1] in have_gem2:
                    have_gem2.append(gems[x1])
                
            min_len_list.append([x1+1,x2+1, x2-x1])
            gems = gems[x2+1:]
            len_gems = len(gems)
            if not len_gems == 0:
                x1, x2, have_gem, have_gem2 = init(gems)
                idx = 0 
            else:
                break
        
        idx += 1

    for i in min_len_list:
        if min_len >= i[2]:
            min_len = i[2]
            answer = i[:2]
    
    return answer

# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# result = [3, 7]

# gems = ["AA", "AB", "AC", "AA", "AC"]
# result = [1, 3]

# gems = ["XYZ", "XYZ", "XYZ"]
# result = [1, 1]

# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# result = [1, 5]

print(solution(gems))