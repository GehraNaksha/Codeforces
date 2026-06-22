t = int(input(""))
for _ in range(t):
    n, x, y, z = map(int, input("").split())
    
    t1 = ((n-x*z)/(x+10*y)+z) 
    
    t2 = n/(x+y)

    print(min(int(-(-t1//1)),int(-(-t2//1))))