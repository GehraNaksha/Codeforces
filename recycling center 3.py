t = int(input(""))
for _ in range (t):
    n, c = map(int, input("").split())
    a = list(map(int, input().split())) 

    for l in range(n):
        coins = 0
        difference =[]
        b = []
        point = float(c/2)        
        for j in range(len(a)):
            d = a[j] - c/2
            b.append(d)

        b.sort()

        for o in range(len(a)):
            if b[o] > 0:           
                recycled = b[o] + point
        for i in range(len(a)):  
            print(i)
            if a[i] == recycled:
                    a.pop(a[i])

        a = [item*2 for item in a]
        print(a)
        print(recycled)

        if recycled > float(c):
            coins = coins +1
        else:
            coins = coins
print(coins)
            
            
        
