from re import A


number = int(input())

for x in range(1, 10):
    print('%d * %d = %d' %(number,x,number*x))