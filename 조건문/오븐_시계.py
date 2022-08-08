hour,min=map(int,input().split(' '))
time = int(input())

if(min+time>=60):
    print((hour+(min+time)//60)%24,(min+time)%60)
else:
    print(hour,min+time)