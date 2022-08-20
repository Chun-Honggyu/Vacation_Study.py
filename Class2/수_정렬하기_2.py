import sys

attempt=int(sys.stdin.readline())
number=[]
for i in range(attempt):
    number.append(int(sys.stdin.readline()))

number.sort()

for i in range(len(number)):
    print(number[i])

'''for i in range(len(number)):
    for j in range(len(number)-i-1):
        if(number[j]>number[j+1]):
            temp = number[j]
            number[j] = number[j+1]
            number[j+1] = temp
for i in range(len(number)):
    print(number[i])'''