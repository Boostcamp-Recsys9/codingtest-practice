from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    info_dict = info_parsing(info)
    for question in query:
        command,score = query_parsing(question)
        if command in info_dict and len(info_dict[command])>0:
            length =len(info_dict[command])
            start=0
            end=len(info_dict[command])-1
            array =info_dict[command]
            index = 0
            while start<=end:
                mid = (start+end)//2
                if array[mid] >=score:
                    end = mid-1
                else:
                    start = mid+1
            answer.append(length-start)
        else:
             answer.append(0)       
    return answer

def info_parsing(info):
    info_dict = defaultdict(list)
    for i in info:
        temp = i.split(" ")
        info_key = temp[:-1]
        info_score = int(temp[-1])
        for k in range(5):
            for case in combinations(info_key,k):
                name = "".join(case)
                info_dict[name].append(int(info_score))
    for key in info_dict.keys():
        info_dict[key].sort()
    return info_dict

def query_parsing(question):
    q_temp = question.split(' and ')
    food,score= q_temp[-1].split(" ")
    command = ""
    for content in q_temp[:-1]:
        if content !="-":
            command+=content
    if food!="-":
        command+=food
    return command,int(score)