t = int(input(""))
for _ in range(t):
    n, a, b = map(int, input().split())
    sum = 0
    c = int((n-n%3)/3)
    d = n%3
    sum1 = n*a
    sum2 = c*b+d*a
    
    if d !=0:
        sum3 = (c+1)*b
    else:
        sum3= c*b
    print(min(sum1,sum2,sum3))