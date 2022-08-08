hour,min = map(int,input().split(' '))

if(min<45):
    print((hour-1)%24,(min+15)%60)
else:
    print((hour)%24,(min-45)%60)

#파이썬은 -n%Number일때 Number-n을 출력