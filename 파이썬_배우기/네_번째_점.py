x=[]
y=[]

for i in range(3):
    x_temp,y_temp=map(int,input().split())
    x.append(x_temp)
    y.append(y_temp)

if(x[0]==x[1]):
    result_x = x[2]
elif(x[1]==x[2]):
    result_x = x[0]
elif(x[0]==x[2]):
    result_x = x[1]

if(y[0]==y[1]):
    result_y = y[2]
elif(y[1]==y[2]):
    result_y = y[0]
elif(y[0]==y[2]):
    result_y = y[1]

print(result_x,result_y)

