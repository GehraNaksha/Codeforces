t = int(input(""))
for _ in range(t):
    n = int(input(""))
    a = list(map(str, input("").split()))
    print(a)
    s = ""
    print(min(a))
    print(len(min(a)))
    for i in range(n):
        a = a