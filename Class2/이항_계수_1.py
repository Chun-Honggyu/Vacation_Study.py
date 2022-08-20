n,k=map(int,input().split())
head = []
result_head=1
result_bottom=1
while(n!=0):
    head.append(n)
    n-=1
for i in range(k):
    result_head*=head[i]
    result_bottom*=i+1
print(result_head//result_bottom)

