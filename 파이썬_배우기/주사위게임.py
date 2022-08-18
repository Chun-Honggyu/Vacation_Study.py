people = int(input())
result=[]
for i in range(people):
    n1,n2,n3 = map(int,input().split())
    if(n1 == n2 == n3):
        prize = 10000+n1*1000
    elif(n1==n2 and n2!=n3):
        prize = 1000+n1*100
    elif(n1!=n2 and n2==n3):
        prize = 1000+n2*100
    elif(n1!=n2 and n1!=n3 and n2!=n3):
        if(n1>n2 and n1>n3):
            prize = n1*100
        elif(n2>n1 and n2>n3):
            prize = n2*100
        else:
            prize = n3*100
    result.append(prize)

max = result[0]

for i in range(len(result)):
    if(result[i]>max):
        max = result[i]

print(max)
    