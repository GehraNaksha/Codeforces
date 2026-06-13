t = int(input(""))
for _ in range(t):
    n = int(input(""))
    b = []
    for i in range(n):
        b.extend([i+1,3*n-1-2*i,3*n-2*i])
    print(*b)