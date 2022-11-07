def solution(board, moves):
    stack = []
    cnt=0
    for order in moves:
        for i in range(len(board)):
            index = board[i][order-1]
            if index==0:
                pass
            else:
                board[i][order-1] = 0
                stack.append(index)
                if len(stack) <2:
                    pass
                else:
                    if stack[-2] == stack[-1]:
                        cnt+=2
                        stack.pop()
                        stack.pop()
                break
    return cnt