import re
def solution(new_id):
    #1
    id1 = new_id.lower()
    #2
    id2 = re.sub('[=+,#/\?:^@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', '', id1)
    #3
    c=0
    id3 =''
    c = 0
    for i in id2:
        if (i == '.') and (c==0):
            c = 1
            id3+=i
        elif (i == '.') and (c>0):
            c = 1
        else:
            c = 0 
            id3+=i
    '''
    l = id2.split(".")
    nl = [c for c in l if c]
    id3 = ".".join(nl)
    '''
    #4
    id3 = id3.strip(".")
    #5
    if id3 == '':
        id3 = 'a'
    #6
    if len(id3)>15:
        id3 = id3[:15]
    id6 = id3.rstrip(".")
    #7
    if len(id6)==1:
        id6 = id6*3
    if len(id6)==2:
        id6 = id6+id6[-1]
    answer = id6
    return answer
