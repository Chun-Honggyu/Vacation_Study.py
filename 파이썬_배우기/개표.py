number = int(input())
grade = input()
A = 0
B = 0
for i in range(number):
    if(grade[i]=='A'):
        A+=1
    else:
        B+=1
if(A>B):
    print('A')
elif(A<B):
    print('B')
else:
    print("Tie")