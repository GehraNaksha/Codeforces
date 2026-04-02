t = int(input(""))
for _ in range(t):
    l, a, b = map(int, input("").split())
    k = 0
    n = (a + k*b)%l
    while n > (l-1-b):
        k+=1
        n = (a + k*b)%l

    print(n-1)