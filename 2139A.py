t = int(input(""))
for _ in range(t):
    a, b = map(int, input().split())
    d = max(a,b)
    e= min(a,b)
    c = d/e
    result = 0
    if c.is_integer() == True and c != 1:
        result = 1
    elif c.is_integer() == False:
        result = 2
    print(result)