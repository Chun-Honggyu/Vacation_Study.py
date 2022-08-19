cnt=0
string = input()
length = len(string)
for i in range(length//2):
    if(string[i]==string[length-1-i]):
        cnt+=1
if(cnt == length//2):
    print(1)
else:
    print(0)