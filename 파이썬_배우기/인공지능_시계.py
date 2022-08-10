hour, min, sec = map(int,input().split())
time = int(input())

add_hour = time//3600
add_min = (time%3600)//60
add_sec = (time%3600)%60

hour += add_hour
min += add_min
sec += add_sec

if(sec>=60):
    min+=sec//60
    sec%=60
if(min>=60):
    hour+=min//60
    min%=60
if(hour >= 24):
    hour%=24

print(hour,min,sec)