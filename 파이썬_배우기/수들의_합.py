summit = int(input())
num = 0
i=1
while(1):
    num+=i
    if(num==summit):
        print(int(i))
        break
    elif(num>summit):
        print(int(i-1))
        break
    else:
        i+=1