total_cost = int(input())
attempt = int(input())
sum=0
for x in range(attempt):
    cost,number = map(int, input().split(' '))
    sum+=cost*number

if(sum == total_cost):
    print("Yes")
else:
    print("No")