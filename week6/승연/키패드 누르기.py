# 01-응용) 키패드 누르기 [2020카카오 인턴쉽 ]
def solution(numbers, hand):
    phone = {
        1:(1,1),
        2:(1,2),
        3:(1,3),
        4:(2,1),
        5:(2,2),
        6:(2,3),
        7:(3,1),
        8:(3,2),
        9:(3,3),
        '*':(4,1),
        0:(4,2),
        '#':(4,3)
    }
    
    l,r = phone['*'],phone['#']
    
    answer = ''
    
    c_l,c_r = l,r
    
    for num in numbers:
        num = int(num)
        if phone[num][1] == 1:
            c_l = phone[num]
            answer += "L"
        elif phone[num][1] == 3:
            c_r = phone[num]
            answer += "R"
        else:
            d_l = abs(phone[num][0] - c_l[0]) + abs(phone[num][1] - c_l[1])
            d_r = abs(phone[num][0] - c_r[0]) + abs(phone[num][1] - c_r[1])
            if d_l > d_r:
                c_r = phone[num]
                answer += "R"
            elif d_r > d_l:
                c_l = phone[num]
                answer += "L"
            else:
                if hand == 'right':
                    c_r = phone[num]
                    answer += "R"
                else:
                    c_l = phone[num]
                    answer += "L"
    return answer