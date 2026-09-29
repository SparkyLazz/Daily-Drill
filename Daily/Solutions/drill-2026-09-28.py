def solve(counts: list[int]) -> int:
    if len(counts) == 0:
        return 0
    strechMax = 1
    strech = 1
    for i in range(len(counts) - 1):
        if counts[i] < counts[i + 1]:
            strech += 1
        else:
            strechMax = max(strechMax, strech)
            strech = 1
    strechMax = max(strechMax, strech)
    return strechMax
exampleList = [1, 1, 1]
print(solve(exampleList))
