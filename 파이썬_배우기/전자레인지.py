sec = int(input())
a = 300
b = 60
c = 10
min5 = sec//a
min1 = (sec%a)//b
sec10 = ((sec%a)%b)//c

if(((sec%a)%b)%c!=0):
    print(-1)
else:
    print(min5,min1,sec10)