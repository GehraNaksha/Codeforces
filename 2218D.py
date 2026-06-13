t = int(input(""))
for _ in range(t):
    n = int(input(""))
    a = []
    for i in range(1,n+1,1):
        a.extend([i*(i+1)])
    print(*a)