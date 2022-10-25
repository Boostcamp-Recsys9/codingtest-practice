def solution(numbers, hand):
    answer = ''
    keypad = [1,2,3,4,5,6,7,8,9,"*",0,"#"]
    left_now = "*"
    right_now = "#"
    for i in numbers:
        if i in [1,4,7]:
            answer += "L"
            left_now = i
        elif i in [3,6,9]:
            answer += "R"
            right_now = i
        else:
            i_ = keypad.index(i)
            l_ = keypad.index(left_now)
            r_ = keypad.index(right_now)
            left_ = abs(i_//3 - l_//3) + abs(i_%3 - l_%3) 
            right_ = abs(i_//3 - r_//3) + abs(i_%3 - r_%3)
            if left_ <= right_:
                answer += "L"
                left_now = i
            elif left_ > right_:
                answer += "R"
                right_now = i
            else:
                if hand == "left":
                    answer += "L"
                    left_now = i  
                else:
                    answer += "R"
                    right_now = i

            

    return answer