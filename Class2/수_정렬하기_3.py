import sys
# 명령의 수(n)
n = int(sys.stdin.readline().rstrip())

# 계수정렬을 하기위하여 리스트 생성
# cnt[4]는 4가 주어진 횟수가 담겨짐
cnt = [0] * 10001

# n번만큼 수를 입력 받음(10,000이하의 자연수)
for _ in range(n) :

    input_data = int(sys.stdin.readline().rstrip())
    # cnt리스트의 입력된 수 인덱스에 접근하여 +1을 해줌. 한 번 입력되었다는 듯
    cnt[input_data] += 1

# 1부터 10,000까지 cnt의 모든 인덱스에 접근하여
# 인덱스 숫자(i)를 cnt[i] 번 반복 해줍니다.
# 0이 아니라면 / 0이라면 입력 받은 적이 없기 때문
for i in range(1, 10001) :
    if cnt[i] != 0:
        for _ in range (cnt[i]):
            print(i)


"""attempt=int(input())
result=[]
for i in range(attempt):
    result.append(int(input()))

count = [0] * (max(result) + 1)

for num in result:
    count[num] += 1

for i in range(1, len(count)):
    count[i] += count[i-1]

final_result = [0] * (len(result))

for num in result:
    idx = count[num]
    final_result[idx - 1] = num
    count[num] -= 1

print(final_result)"""


'''for i in range(len(result)):
    swapped = False
    for j in range(len(result)-i-1):
        if(result[j]>result[j+1]):
            temp = result[j+1]
            result[j+1] = result[j]
            result[j] = temp
            swapped = True
    if(swapped == False):
        break
for i in range(len(result)):
    print(result[i])'''