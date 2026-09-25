def solve(counts: list[int]) -> int:
    max = 0
    diff = 0
    for i in range(len(counts)):
        if counts[i] > max:
            max = counts[i]
        currentDiff = max - counts[i]
        if currentDiff > diff:
            diff = currentDiff
    return diff

#Example usage:
counts = [3, 5, 2, 8, 6]
result = solve(counts)
print(result)
