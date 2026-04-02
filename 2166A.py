t = int(input(""))
for _ in range(t):
    n = int(input(""))
    s = input("")
    freq = [s.count(item) for item in s]
    a = freq.index(max(freq))
    print(a)
    count = 0
    count1 = 0
    for i in range(n):
        print(s[i], s[a])
        if freq[i] == max(freq):
            print("ello")
            if s[i] != s[a]:
                print(count)
                count +=1
            else:
                count1 +=1
                print("ola")
        else:
            count1 +=1

    print(count)
    print(n-count1)