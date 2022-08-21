M, N = map(int, input().split())

def prime_list(n):
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return [i for i in range(M, n + 1) if sieve[i] == True]
li = prime_list(N)
if 1 in li:
    li.remove(1)
    for k in li:
        print(k)
else:
    for _ in prime_list(N):
        print(_)