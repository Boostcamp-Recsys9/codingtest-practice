def solution(numbers, hand):
    arrayL = [1,4,7]
    arrayR = [3,6,9]
    array = [2,5,8,0]
    answer = ''
    cursorL = [3,0]
    cursorR = [3,2]
    cursor = [0,0]
    tempL = [0,0]
    tempR = [0,0]
    for i in numbers:
        if(i in arrayL):
            answer += 'L'
            cursorL = [i // 3, 0]
        elif(i in arrayR):
            answer += 'R'
            cursorR = [(i // 3 - 1), 2]
        elif(i in array):
            if(i == 0):
                cursor = [3,1]
            else:
                cursor = [i//3, 1]
            tempL = [abs(cursor[0] - cursorL[0]), abs(cursor[1] - cursorL[1])]
            tempR = [abs(cursor[0] - cursorR[0]), abs(cursor[1] - cursorR[1])]
            if((tempL[0] + tempL[1]) < (tempR[0] + tempR[1])):
                answer += 'L'
                cursorL = cursor
            elif((tempL[0] + tempL[1]) > (tempR[0] + tempR[1])):
                answer += 'R'
                cursorR = cursor
            else:
                if(hand == 'left'):
                    answer += 'L'
                    cursorL = cursor
                else:
                    answer += 'R'
                    cursorR = cursor
    return answer