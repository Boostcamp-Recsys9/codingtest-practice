def solution(board, skill):
    answer = 0
    row = len(board[0])
    column=len(board)
    skilled_array = prefix_sum(skill,row,column)
    for i in range(column):
        for j in range(row):
            board[i][j] += skilled_array[i][j]
            if board[i][j] >0:
                answer+=1
    return answer



def prefix_sum(skill,row,column):
    prefix_array = [[0 for _ in range(row+1)] for _ in range(column+1)]
    for skill_type,r1,c1,r2,c2,degree in skill:
        prefix_array[r1][c1] += degree if skill_type>1 else -degree
        prefix_array[r1][c2+1] -= degree if skill_type>1 else -degree
        prefix_array[r2+1][c1] -= degree if skill_type>1 else -degree
        prefix_array[r2+1][c2+1] += degree if skill_type>1 else -degree 
        
    for i in range(column+1):
        for j in range(row):
            prefix_array[i][j+1] += prefix_array[i][j]
    for j in range(row+1):
        for i in range(column):
            prefix_array[i+1][j] += prefix_array[i][j] 
    return prefix_array