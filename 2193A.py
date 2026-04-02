t = int(input(""))
for _ in range(t):
    n, s, x = map(int, input("").split())
    a = list(map(int, input("").split()))
    sum = 0
    for i in range(n):
        sum += a[i]
    diff = s -sum
    if diff >= 0:
        if diff%x == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
