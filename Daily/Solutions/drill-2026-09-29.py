def solve (weights: list[int]) -> int:
    firstHeight = -1
    secondHeight = -1
    for i in range(len(weights)):
        if weights[i] > firstHeight:
            secondHeight = firstHeight
            firstHeight = weights[i]
        elif weights[i] > secondHeight and weights[i] != firstHeight:
            secondHeight = weights[i]
    return secondHeight
data = []
result = solve(data)
print(result)  # Output: 4
