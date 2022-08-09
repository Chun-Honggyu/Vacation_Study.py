origin = int(input())
number = origin
cnt=0
while(1):
    ten = number//10
    one = number%10
    number = one*10+(ten+one)%10
    cnt+=1
    if(number == origin):
        break
print(cnt)