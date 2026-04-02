t = int(input(""))
for _ in range(t):
    n = int(input(""))
    a = list(map(int,input("").split()))
    for i in range(1,n-1):
        x = a[i-1]
        y = a[i]
        z = a[i+1]
        o = a[i+2]

        if x==(z + 1) or z ==(x+1):
            result = "NO"
            break
        elif y ==(o+1) or o ==(y+1):
            result = "NO"
            break
        else:
            result = "YES"
        i+=5
    print(result)