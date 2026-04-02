testCases = int(input(""))

for i in range(testCases):
    coins = 0
    n, c = map(int, input().split())
    weights = list(map(int, input().split()))
    referenceWeights = weights
    
    length = len(referenceWeights)
    weights.sort()

    for iterator in range(length):
        lightWeight = [] 
        for weight in weights:
            if weight <= c:
                lightWeight.append(weight)
        
        lightWeight.sort(reverse=True)
        if lightWeight:
            weights.remove(lightWeight[0])
        else:
            weights.pop(0)
            coins+= 1
       
        for remainingWeightindex in range(len(weights)):
            weights[remainingWeightindex] = weights[remainingWeightindex]*2
        
    print(coins)