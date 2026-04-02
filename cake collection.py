t = int(input(""))

for _ in range(t):

    n, m = map(int, input().split())
    increment = list(map(int, input().split()))
    reference_cakes = [0 for item in increment]
    cakes = 0

    #NEED TO LEARN GREEDY ALGORITHIMS FIRST
    #only then its possible to solve this
    #because imo till my knowledge the best way to ensure u get the maximum of something in total is
    #to make sure that ur getting maximum of it at each possible moment ie most cakes at the end of each second currently present in the oven 
    #does my program need to be.... smart?


    for _ in range(m-n+1):

        for i in range(len(increment)):
            reference_cakes[i] += increment[i]

        cakes += max(reference_cakes)

        for i in range(len(reference_cakes)):
            if reference_cakes[i] == max(reference_cakes):
                reference_cakes[i] = 0

    for i in range(len(reference_cakes)):
        cakes = cakes + reference_cakes[i]
        reference_cakes[i] = 0

        for j in range(len(reference_cakes)):
            reference_cakes[j] = reference_cakes[j] + increment[j]

    print(cakes)