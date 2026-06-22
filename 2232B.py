t = int(input(""))
for _ in range(t):
    n = int(input(""))
    a= list(map(int, input("").split()))
    b = []
    sum = 0
    max = 10**9+1
    for i in range(n):
        sum += a[i]
        
        avg = int(sum/(i+1))
        max = min(max,avg)
        b.append(max)
    print(*b)
