t = int(input(""))

for _ in range(t):

    n = int(input(""))
    colors = []

    for i in range(n):

        a = list(map(int, input("").split()))
        colors.extend(a)
    
    max_freq = max(colors.count(i) for i in range(len(colors))) 

    if max_freq > (n**2-n) or n==1:

        print("NO")
    else:

        print("Yes")
