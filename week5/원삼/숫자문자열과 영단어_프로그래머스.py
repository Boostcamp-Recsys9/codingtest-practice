def solution(s):
    # 간단하게 리스트 replace하기
    str_list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for y in range(10):
        s = s.replace(str_list[y],str(y))
    return int(s)