t = int(input(""))
for _ in range(t):
    n = int(input(""))
    a = list(map(int, input("").split()))
    
    score = 0
    mex =0
    for i in range(0,n,1):
        if a[i] == mex:
            score+=1
        else:
            score+=a[i]

    print(score)