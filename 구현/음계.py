music = []
ascending=0
decending=0
music = list(map(int,input().split()))
for i in range(8):
    if(i<7):
        if(music[i+1]==music[i]+1):
            ascending+=1
        elif(music[i+1]==music[i]-1):
            decending+=1
    else:
        if(music[i]==music[i-1]+1):
            ascending+=1
        elif(music[i]==music[i-1]-1):
            decending+=1
if(ascending==8):
    print("ascending")
elif(decending==8):
    print("descending")
else:
    print("mixed")


