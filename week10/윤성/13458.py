n=int(input())
people = list(map(int,input().split()))
b,c =map(int,input().split())
count = 0
for i in range(len(people)):
    people[i]=max(people[i]-b,0)
    count+=1
    if people[i] >0:
        if people[i] % c ==0:
            count+=(people[i] // c)
        else:
            count+=(people[i] // c)+1
print(count) 