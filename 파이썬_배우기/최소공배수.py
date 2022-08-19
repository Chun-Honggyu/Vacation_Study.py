from math import lcm

attempt = int(input())

for i in range(attempt):
    x,y=map(int,input().split())
    print(lcm(x,y))