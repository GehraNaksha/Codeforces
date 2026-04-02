##2167A
t = int(input(""))
for _ in range(t):
    a, b, c, d = map(int, input('').split())
    if a == b == c == d:
        print("YES")
    else:
        print("NO")


##2167B
q = int(input(""))
for _ in range(q):
    n = int(input(""))
    s, t = input("").split(' ')
    a = 'YES'
    for i in range(n):
        if t[i] not in s:
            a = 'NO'
            break
        else:
           s=  s.replace(t[i], '',1)
    print(a)
