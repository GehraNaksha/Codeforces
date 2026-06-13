t = int(input(""))
for _ in range(t):
    n = int(input(""))
    a = list(map(int, input("").split()))
    i = 1
    result = a[n-1]
    for i in range(n-1):
        result^=a[i]

    print(result)