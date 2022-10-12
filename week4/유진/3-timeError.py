def solution(info, query):
    answer = [0 for i in range(len(query))]
    info_list = []
    query_list = []
    for i in range(len(info)):
        info_list.append(info[i].split())
    for j in range(len(query)):
        query_list.append(query[j].split())
        while len(query_list[j]) > 5:
            query_list[j].remove("and")

    for i in range(len(info_list)):
        for j in range(len(query_list)):
            no_strings = False
            for k in range(4):
                if info_list[i][k] != query_list[j][k]:
                    if query_list[j][k] != '-':
                        no_strings = True
                        break
            if no_strings == False :
                if int(info_list[i][4]) >= int(query_list[j][4]):
                    answer[j] += 1

    return answer