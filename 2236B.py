t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    count = [0] * k

    for i in range(n):

        count[i % k] += int(s[i])
    result = all(c % 2 == 0 for c in count)

    print("YES" if result else "NO")