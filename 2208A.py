t = int(input(""))

for _ in range(t):
    n = int(input(""))
    
    freq = {}
    max_freq = 0

    for i in range(n):
        a = list(map(int, input("").split()))
        for color in a:
            
            freq[color] = freq.get(color, 0) + 1
            
            if freq[color] > max_freq:
                max_freq = freq[color]
    
    if max_freq > (n**2 - n) or n == 1:
        print("NO")
    else:
        print("YES")
