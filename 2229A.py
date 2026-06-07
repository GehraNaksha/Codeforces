t = int(input(""))
for _ in range(t):
    n = int(input(""))
    a = list(map(int, input().split()))
    
    max1 = max(a)
    min1 = min(a)
    sum = max1+min1
    x = round(sum/2)
    diff1 = abs(max1-x)
    diff2 =abs(min1-x)
    print(max(diff1,diff2))