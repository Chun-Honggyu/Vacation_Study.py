height = 10
plate = input()
if(plate[0]=='('):
    for i in range(1,len(plate)):
        if(plate[i]==plate[i-1]):
            height+=5
        else:
            height+=10
elif(plate[0]==')'):
    for i in range(1,len(plate)):
        if(plate[i]==plate[i-1]):
            height+=5
        else:
            height+=10
print(height)