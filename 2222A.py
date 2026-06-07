t = int(input(""))
for _ in range(t):
    n = int(input(""))
    a = list(map(int, input("").split()))
    b = 100
    if b in a:
        print("YES")
    else:
        print("NO")