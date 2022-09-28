def solution(id_list, report, k):
    answer = []
    table = {i:[] for i in id_list}
    answer_table={i:0 for i in id_list}
    for users in report:
        user,report_user = users.split(" ")
        if not user in table[report_user]:
            table[report_user].append(user)
    for users in table:
        if len(table[users])>=k:
            for m in table[users]:
                answer_table[m]+=1
    answer = [i for i in answer_table.values()]
    return answer