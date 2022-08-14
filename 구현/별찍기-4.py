star = int(input())
for i in range(star):
    for j in range(i):
        print(' ',end='')
    for k in range(star-i):
        print('*',end='')
    print('')