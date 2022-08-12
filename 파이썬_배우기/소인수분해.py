number = int(input())
cnt = 0
prime = []

for i in range(2,10000000):
    cnt = 0
    for j in range(2,i+1):
        if(i%j == 0):
            cnt+=1
    if(cnt == 1):
        prime.append(i)

i=0
while(number!=1):
    if(prime[i]<=number):
        if(number%prime[i] == 0):
            print(prime[i])
            number/=prime[i]
            i=0
        else:
            continue
    else:
        i+=1