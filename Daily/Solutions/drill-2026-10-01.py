def solve(readings: list[int]) -> int:
    if not readings:
        return 0
    max = readings[0]
    records = 1
    for i in range(len(readings)):
        if readings[i] > max:
            max = readings[i]
            records += 1
    return records

test = [3, 1, 4, 4, 7]
print(solve(test))  # Output: 3
