number = []
sum=0
number = list(map(int, input().split()))
for i in range(5):
    number[i]*=number[i]

    sum+=number[i]
print(sum%10)
