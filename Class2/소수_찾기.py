number = int(input())

temp=[]
cnt=0
result_cnt=0

temp = list(map(int,input().split()))

for i in range(len(temp)):
    cnt=0
    for j in range(2,temp[i]+1):
        if(temp[i]%j==0):
            cnt+=1
    if(cnt==1):
        result_cnt+=1
        
print(result_cnt)