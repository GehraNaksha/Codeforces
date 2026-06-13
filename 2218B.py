t = int(input(""))
for _ in range(t):
    a = list(map(int, input("").split()))
    max1 = max(a)
    result = (sum(a) -2*max1)*-1
    print(result) 