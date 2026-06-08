t =int(input(""))
for _ in range(t):
    n = int(input(""))
    a = list(map(int, input("").split()))
    by6 = []
    by3= []
    by2= []
    by = []
    for i in a:
        if i % 6== 0:
            by6.append(i)
        elif i%2 == 0:
            by2.append(i)
        elif i%3==0:
            by3.append(i)
        else:
            by.append(i)
    b = []
    b.extend(by6)
    b.extend(by2)
    b.extend(by)
    b.extend(by3)
    print(*b)