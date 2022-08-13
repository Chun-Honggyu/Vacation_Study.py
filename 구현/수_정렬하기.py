temp = []
attempt = int(input())
for i in range(attempt):
    temp.append(int(input()))
temp.sort()
for i in range(attempt):
    print(temp[i])