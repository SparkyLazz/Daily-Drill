def solve(bowls: list[int]) -> int:
    if len(bowls) < 2:
        return 0
    last = ""
    current = ""
    turn = 0
    for i in range(len(bowls) - 1):
        if bowls[i] > bowls[i + 1]:
            current = "decreasing"
            if last == "increasing":
                turn += 1
            last = current
        elif bowls[i] < bowls[i + 1]:
            current = "increasing"
            if last == "decreasing":
                turn += 1
            last = current
    return turn

bowls = [2, 5, 3, 3, 7]
print(solve(bowls))
