def solve(climbs: list[int]) -> int:
    currentHeight = 0
    currentMax = 0
    for i in range(len(climbs)):
        currentHeight += climbs[i]
        if currentHeight > 0:
            currentMax = max(currentMax, currentHeight)
    return currentMax

climbs =  [3, -1, 4, -6, 2]
print(solve(climbs))
