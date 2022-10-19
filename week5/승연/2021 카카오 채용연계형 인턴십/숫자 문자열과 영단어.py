def solution(s):
    answer = ""
    word = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }

    c = ""
    for t in s:
        if t.isdigit():
            answer += t
            continue
        c+=t
        if c in word.keys():
            answer += word[c]
            c = ""

    answer = int(answer)
    return answer



sl = ["one4seveneight", '23four5six7', '2three45sixseven', '123']
for s in sl:
    print(solution(s))