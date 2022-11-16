from itertools import product
from copy import deepcopy

def max_linear(array):
    result = []
    for content in array:
        result += content
    return max(result)

def move_column_left(array):
    for i in range(n):
        index = []
        for opt in range(n):
            if array[i][opt] > 0:
                index.append(opt)
        k=1
        while k < len(index):
            if array[i][index[k-1]] == array[i][index[k]]:
                array[i][index[k-1]] *=2
                array[i][index[k]]=0
                k+=2
            else:
                k+=1
        temp = []
        for j in range(n):
            if array[i][j] > 0:
                temp.append(array[i][j])
        for _ in range(n-len(temp)):
            temp.append(0)
        array[i] = temp
    return array

def move_column_right(array):
    for i in range(n):
        index = []
        for opt in range(n):
            if array[i][opt] > 0:
                index.append(opt)
        k=len(index)-1
        while k > 0:
            if array[i][index[k-1]] == array[i][index[k]]:
                array[i][index[k]] *=2
                array[i][index[k-1]]=0
                k-=2
            else:
                k-=1
        temp = []
        for j in range(n):
            if array[i][j] > 0:
                temp.append(array[i][j])
        blank = [0] * (n-len(temp))
        temp = blank+temp
        array[i] = temp
    return array

def move_row_up(array):
    for i in range(n):
        index = []
        for opt in range(n):
            if array[opt][i] > 0:
                index.append(opt)
        k=1
        while k < len(index):
            if array[index[k-1]][i] == array[index[k]][i]:
                array[index[k-1]][i] *=2
                array[index[k]][i]=0
                k+=2
            else:
                k+=1
        temp = []
        for j in range(n):
            if array[j][i] > 0:
                temp.append(array[j][i])
        for _ in range(n-len(temp)):
            temp.append(0)
        for m in range(n):
            array[m][i] = temp[m]
    return array

def move_row_down(array):
    for i in range(n):
        index = []
        for opt in range(n):
            if array[opt][i] > 0:
                index.append(opt)
        k=len(index)-1
        while k > 0:
            if array[index[k-1]][i] == array[index[k]][i]:
                array[index[k]][i] *=2
                array[index[k-1]][i]=0
                k-=2
            else:
                k-=1
        temp = []
        for j in range(n):
            if array[j][i] > 0:
                temp.append(array[j][i])
        blank = [0] * (n-len(temp))
        temp = blank+temp
        for m in range(n):
            array[m][i] = temp[m]
    return array

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
index = [0,1,2,3]
answer_list = []
protocol = list(set(product(index,repeat=5)))
for content in protocol:
    array_temp=deepcopy(array)
    for opt in content:
        if opt ==0:
            array_temp=move_column_left(array_temp)
        elif opt==1:
            array_temp=move_column_right(array_temp)
        elif opt==2:
            array_temp=move_row_up(array_temp)
        else:
            array_temp=move_row_down(array_temp)
    answer_list.append(max_linear(array_temp))
print(max(answer_list))