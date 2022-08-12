attempt = int(input())
mars = []
for i in range(attempt):
    mars = list(input().split())
    num = float(mars[0])
    for j in range(1,len(mars)):
        if(mars[j]=='@'):
            num*=3
        elif(mars[j]=='%'):
            num+=5
        elif(mars[j]=='#'):
            num-=7
    print("%0.2f" %num)
