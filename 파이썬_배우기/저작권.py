music,avg=map(float,input().split())

melody = music * (avg-0.999999)
print(int(melody)+1)