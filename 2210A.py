t = int(input(""))
for _ in range(t):
    n, a, b = map(int, input().split())
    sum = 0
    bs = (n-n%3)/3
    if a > (b/3):
        sum += b*bs
        if a>(b/2) and n%3==2:
            sum += b
        elif n%3 == 1 and a>b:
            sum += b
        else:
            sum += (n%3)*a

    elif n%3 ==0:
        sum += (bs)*b
    else:
        sum += (bs+1)*b
    print(int(sum))