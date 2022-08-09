number, origin = map(int, input().split())
Arr = list(map(int,input().split()))
    
for i in range(number):
    if(Arr[i]<origin):
        print(Arr[i] ,end=' ')