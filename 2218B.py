t = int(input(""))
for _ in range(t):
    a = list(map(int, input("").split()))
    am = max(a)
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    sum -= 2*am
    print(-1*sum)