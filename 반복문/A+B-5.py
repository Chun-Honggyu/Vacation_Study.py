while 1:
    try:
        n1,n2 = map(int,input().split(' '))
        print(n1+n2)
    except:
        break

#try, except - 에러가 나면 except쪽 코드 실행