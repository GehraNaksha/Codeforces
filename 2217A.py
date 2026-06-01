t = int(input(""))
for _ in range(t):
    n, k = map(int, input("").split())
    a = list(map(int, input("").split()))
    sum1 = 0
    for i in range(n):
        sum1 += a[i]
    sum2 = n*k
    if sum1%2 == 1:
        print("YES")
    elif sum1%2==0 and k%2 ==0:
        print("YES")
    elif sum1%2 ==0 and sum2%2==0:
        print("YES")
    else:
        print("NO")