t = int(input(""))

for _ in range(t):

    n = int(input(""))
    a = list(map(int, input("").split()))
    
    b = []    
    sign = 1
    
    for i in range(n - 1, -1, -1):
        current_val = a[i] * sign
    
        if current_val > 0:
            b.append(i + 1)
            sign *= -1  
            
    print(len(b))
    print(*b)
