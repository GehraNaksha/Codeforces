t = int(input(""))
for o in range (t):
    n , c= map(int, input("").split())
    while n > 30 and c > 10**9:
        n , c=  map(int, input("").split())
    a= list(map(int, input().split()))
    while len(a) > n or len(a) < n:
        a = list(map(int, input().split())) 
    coins = 0
    #sorted in decreasing order
    for i in range(n-1):
        for i in range(n-1):
            if a[i] < a[i+1]:
                a[i], a[i+1] = a[i+1], a[i] 
    #now if say i start the recycling process with numbers either equal to or less than c
    #and once those are finished i move to say numbers which started by being bigger than c
    for i in range(n-1):
        for i in range(n-1):
            if a[i] >c:
                a[i], a[i+1] = a[i+1], a[i]
    print(a)
    for i in range(n):
        if a[i] > c:
            coins = coins +1
            a = [x*2 for x in a]
        else:
            a = [x*2 for x in a]
        print(a)
    print(coins)
