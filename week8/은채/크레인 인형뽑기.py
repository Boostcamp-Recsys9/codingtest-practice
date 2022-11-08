def solution(board, moves):
    ans = [-1]
    count = 0
    for m in moves:
        i = 0
        while i < len(board):
            if board[i][m-1] != 0:
                d = board[i][m-1]
                board[i][m-1] = 0
                if ans[-1] == d:
                    print("pop",ans.pop(-1))
                    count+=1
                else:
                    ans.append(d)
                print(d)
                break
            else:
                i+=1
    return count * 2
