t = int(input(""))
for _ in range(t):
    n, c = map(int, input("").split())
    a = list(map(int, input("").split()))

    for _ in range(n):
        coins = 0
        a.sort(reverse=True)
        if a[0] > c and len(a) >= 1:
            coins +=1
            a.pop(a[0])
        else:
            a.pop(a[0])
    print(coins)