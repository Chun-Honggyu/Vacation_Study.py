while(1):
    number = int(input())
    if(number==0):
        break
    len=0
    cnt=0
    temp = number
    result = []
    while(temp!=0):
        temp = temp//10
        len+=1
    for i in range(len):
        result.append(number%10)
        number = number//10
    for i in range(len//2):
        if(result[i]==result[len-1-i]):
            cnt+=1
    if(cnt == len//2):
        print("yes")
    else:
        print("no")
