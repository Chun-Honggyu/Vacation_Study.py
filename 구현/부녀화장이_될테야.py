attempt = int(input())
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in range(attempt):
    floor = int(input())
    room = int(input())
    if(floor == 0):
        print(number[room+1])
    else:
        for i in range(floor):
            for j in range(14):
                if(j==0):
                    number.append(1)
                else:
                    number.append(number[13+j]+number[j])
            for k in range(14):
                del number[0]
    print(number[room-1])
    number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]


