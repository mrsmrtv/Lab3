def solve(numheads, numlegs):
    
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits 
heads = 35
legs = 94
print(solve(heads, legs))
