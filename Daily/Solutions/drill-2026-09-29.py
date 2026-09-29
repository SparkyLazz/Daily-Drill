def solve (weights: list[int]) -> int:
    firstHeight = weights[0]
    secondHeight = weights[0]
    for i in range(len(weights)):
        if weights[i] > firstHeight:
            secondHeight = firstHeight
            firstHeight = weights[i]
        elif weights[i] > secondHeight and weights[i] != firstHeight:
            secondHeight = weights[i]
    return secondHeight
data = [4, 9, 9, 2, 7]
result = solve(data)
print(result)  # Output: 4
