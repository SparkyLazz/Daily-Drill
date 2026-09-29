def solve (weights: list[int]) -> int:
    integerMax = max(weights)
    indicate = 0
    for i in range(len(weights)):
        if weights[i] > indicate and weights[i] < integerMax:
            indicate = weights[i]
    return indicate

data = [4, 9, 9, 2, 7]
result = solve(data)
print(result)  # Output: 4
