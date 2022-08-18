while(1):
    result=[]
    sum=0
    number = int(input())
    if(number==-1):
        break
    for i in range(1,number):
        if(number%i == 0):
            result.append(i)
    for i in range(len(result)):
        sum+=result[i]
    if(sum == number):
        print(f"{number} = ",end='')
        for i in range(len(result)):
            print(result[i],end=' ')
            if(i == len(result)-1):
                break
            print('+',end=' ')
    else:
        print(f"{number} is NOT perfect.")
