def solve(nums: list[int]) -> int:
    if len(nums) == 0:
      return -1
    largestNumberIndex = 0
    for i in range(len(nums)):
        if nums[i] >= nums[largestNumberIndex]:
            largestNumberIndex = i
    return largestNumberIndex

print(solve([3, 7, 2, 7, 5]))
print(solve([-4, -4, -9]))
print(solve([]))
print(solve([5]))
