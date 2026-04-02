#correct soln

g, c, l = map(int, input("").split())
scores = list((g, c, l))
scores.sort()
if scores[-1] - scores[0] < 10:
    print("final", scores[1])
else:
    print("check again")
