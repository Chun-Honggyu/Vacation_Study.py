a = int(input())
b = int(input())

one = a*(b%10)
two = a*(b%100//10)
three = a*(b//100)

print(one)
print(two)
print(three)
print(a*b)