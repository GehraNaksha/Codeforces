t = int(input(""))
for _ in range(t):
    n = int(input(""))
    w = list(map(int, input("").split()))
    op = w.count(0) 
    while abs(w.count(2)-w.count(1)) >= 3:
        if w.count(2) > w.count(1):
            op +=1
            for i in range(3):
                w.remove(2)
        else:
            op+=1
            for i in range(3):
                w.remove(1)
    op += min(w.count(1),w.count(2))
    print(op)
