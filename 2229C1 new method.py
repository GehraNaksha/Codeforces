t = int(input(""))
for _ in range(t):
    n = int(input(""))
    a = list(map(int, input("").split()))
    test = [a.index(i)+1 for i in a if i>0]
    b = test.copy()
    
    for i in range(len(test)-1,-1,-1):
        
        max1 = test[i]
        print(max1)

        for j in range(a[a.index(max1)-1],-1,-1):
            print(j)
            if a[j] < 0:
                if j in b:
                    b.remove(max1)
                    print("allahi")
                else:
                    b.append(j)
                    print("wallahi")
    print(len(b))
    print(*b)