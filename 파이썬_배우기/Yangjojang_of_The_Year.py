attempt = int(input())
for i in range(attempt):
    school = int(input())
    name = []
    number = []
    for j in range(school):
        school_name,Yangjo = input().split()
        name.append(school_name)
        number.append(int(Yangjo))
    max = number[0]
    result = 0
    for k in range(school):
        if (max<number[k]):
            max = number[k]
            result = k
    print(name[result])

