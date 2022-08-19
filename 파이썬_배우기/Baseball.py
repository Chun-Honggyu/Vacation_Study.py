attempt = int(input())

Yonsei_sum = 0
Korea_sum = 0

for j in range(attempt):
    for i in range(9):
        temp_y,temp_x = map(int,input().split())
        Yonsei_sum+=temp_y
        Korea_sum+=temp_x

    if(Yonsei_sum>Korea_sum):
        print("Yonsei")
    elif(Yonsei_sum<Korea_sum):
        print("Korea")
    else:
        print("Draw")