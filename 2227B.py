t = int(input(""))
for _ in range(t):
    n = int(input(""))
    s = input("")
    a = s.count('(')
    b = s.count(')')
    if a == b:
        print("YES")
    else:
        print("NO")