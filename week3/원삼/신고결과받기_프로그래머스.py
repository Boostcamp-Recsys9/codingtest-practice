def solution(id_list, report, k):
    # 신고당한 수를 저장하는 dict과 이메일 보낼 수를 저장하는 dict생성
    report_dict = {i:0 for i in id_list}
    email_dict = {i:0 for i in id_list}
    # set으로 중복제거 ~
    report = set(report)
    # 신고당했으면 dict에 count
    for i in report:
        report_dict[i.split()[1]] += 1
    # 원래는 이중for문 돌리려고 했으나 시간초과가 (당연히)나서 for문을 쪼개기
    # k번 이상 신고 당하지 않은 것들에 대해 삭제
    for x,y in list(report_dict.items()):
        if y < k:
            del report_dict[x]
    # 정지 대상자들을 신고한 사람들을 이메일 전송 dict에 count       
    for s in report:
        if s.split()[1] in report_dict.keys():
            email_dict[s.split()[0]] += 1
                    
    return list(email_dict.values())
        