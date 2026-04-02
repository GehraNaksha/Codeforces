#correct soln

y= int(input(""))
for t in range(y):
    x = int(input(""))
    i = x%100
    c = x%10
    b = (i -c)/10
    a = (x- i)/100
    if a ==0:
        if a == 0 and b ==0:
            print(int(c))
        elif a == 0 and b <=c:
            print(int(b))
        elif a == 0 and b>=c:
            print(c)
    elif a >= b and b <= c:
        print(int(b))
    elif a <= b and a <= c:
        print(int(a))
    elif c <= a and c <= b:
        print(c)
