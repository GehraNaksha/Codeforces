t = int(input(""))
for _ in range(t):
    k, x = map(int, input("").split())
    i = 0
    while x != 1:
        if x%2 == 0:
            x = x/2
        else:
            x = 3*x + 1

        i += 1
#now i want to reverse engineer the same thing so that if say (x-1)/3 = x is odd then take it otherwise if x = 2*x (will always be even fu
# so to reverse engineer ill have to do 2 diff if loops rather than a if and 1 elif 
    a = x
    b = x
    while i >= 0:
        if a%3 == 2 and (a-1)/3 in range(0,1000):
            a = (a-1)/3
        
        b = b*2
        i -= 1
    print(int(a), int(b))

    #fuckkkkk i hate this
    # i cant even fucking dry run this cuz wtf
    #ofc i can but i dont fucking iwanna man
