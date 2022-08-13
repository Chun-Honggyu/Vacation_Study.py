attempt = int(input())

for i in range(attempt):
    h,w,num = map(int,input().split())
    if(num%h==0):
        floor = h
    else:
        floor = num%h
    
    if(num%h==0):
        room = num//h
    else:
        room = num//h+1

    if(room<10):
        print(str(floor)+'0'+str(room))
    else:
        print(str(floor)+str(room))
    

