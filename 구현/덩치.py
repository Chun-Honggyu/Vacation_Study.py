weight = []
height = []
score = []
result = []
people = int(input())

for k in range(people):
    score.append(0)
    result.append(0)

for i in range(people):
    weight_temp, height_temp = map(int, input().split())
    weight.append(weight_temp)
    height.append(height_temp)

for x in range(people):
    for y in range(people):
        if(weight[x]<weight[y] and height[x]<height[y]):
            score[x]+=1

for i in range(people):
    print(score[i]+1, end=' ')
