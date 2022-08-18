attempt = int(input())
cnt_one=0
cnt_zero = 0
for i in range(attempt):
    info = int(input())
    if(info == 0):
        cnt_zero+=1
    elif(info == 1):
        cnt_one+=1
if(cnt_one>cnt_zero):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
