#correct soln

t = int(input(""))
for _ in range(t):
    x , n = map(int, input("").split())
    if n%2 == 1:
        print(x)
    elif n%2 == 0:
        print(0)
