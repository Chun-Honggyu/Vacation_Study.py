number, pole = map(int,input().split())
card_number=[]
card_sum=[]

card_number = list(map(int,input().split()))

for i in range(len(card_number)-2):
    for j in range(i+1,len(card_number)-1):
        for k in range(j+1,len(card_number)):
            card_sum.append(card_number[i]+card_number[j]+card_number[k])

for m in range(len(card_sum)):
    card_sum[m]-=pole
    if(card_sum[m]>0):
        card_sum[m]-=99999

print(max(card_sum)+pole)

