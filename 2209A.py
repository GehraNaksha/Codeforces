t = int(input(""))
for _ in range(t):
    n, c, k= map(int, input("").split())
    a = list(map(int, input("").split()))
    while len(a) >=1:
        
        if min(a) <= c:
    
            b = a.index(min(a))
            while a[b] != c:
                
                if k>=1:
                    diff = abs(c-a[b])
                    max1 = min(diff,k)
                    a[b] += max1
                    k -= max1
                    break
                else:
                    break
            c+= a[b]
            a.remove(a[b])
        else:
            break
    print(c)
    
##solved this in like 15 mins, proud of it dk why