t = int(input(""))
for _ in range(t):
    n = int(input(""))
    a = list(map(int, input("").split()))
    b = list(map(int, input("").split()))
    sum = 0
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
        sum +=b[i]
    sum += max(a)
    print(sum)