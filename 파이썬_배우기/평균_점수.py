score  = list()

for i in range(5):
    score.append(int(input()))
    if(score[i]<40):
        score[i] = 40

    
summit = sum(score)
avg  = summit/5
print(int(avg))