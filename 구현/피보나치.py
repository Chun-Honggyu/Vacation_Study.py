number = int(input())
result = []
for i in range(number+2):
    if(i==0):
        result.append(i)
    elif(i==1):
        result.append(i)
    else:
        result.append(result[i-1]+result[i-2])

print(result[number])
        