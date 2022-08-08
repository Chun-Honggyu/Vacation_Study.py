one,two,three=map(int,input().split(' '))
if(one==two==three):
    print(10000+one*1000)
elif(one==two and one!=three):
    print(1000+one*100)
elif(one==three and one!=two):
    print(1000+one*100)
elif(one!=two and two==three):
    print(1000+two*100)
else:
    if(one>two and one>three):
        print(one*100)
    elif(two>one and two >three):
        print(two*100)
    elif(three>one and three>two):
        print(three*100)