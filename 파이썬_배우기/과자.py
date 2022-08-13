snack, number, money = map(int,input().split())

total = snack*number
if(total<=money):
    print('0')
else:
    print(total-money)
