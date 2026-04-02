t = int(input(""))
for _ in range(t):
    count = 0
    n = int(input(""))
    for i in range(int(n/2)+1):
        for j in range(int(n/4)+1):
            if (2*i + 4*j) == n:
                count +=1 
    print(count)