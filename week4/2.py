from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for count in course:
        order_list=[]
        for order in orders:
            for content in combinations(order,count):
                order_list.append("".join(sorted(content)))
        order_count = Counter(order_list).most_common()
        max_count=0
        for content in order_count:
            max_count = max(content[1],max_count)
        for content in order_count:
            if content[1]>=max_count and content[1]>1:
                answer.append(content[0])
    answer.sort()
    return answer