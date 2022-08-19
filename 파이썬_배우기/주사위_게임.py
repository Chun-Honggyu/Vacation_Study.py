round = int(input())
person1 = 100
person2 = 100
for i in range(round):
    n1,n2 = map(int, input().split())
    if(n1>n2):
        person2-=n1
    elif(n1<n2):
        person1-=n2
    else:
        continue
print(person1)
print(person2)
    