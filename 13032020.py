def sortNums(nums):
  # Fill this in.
    ones = []
    twos = []
    threes = []
    for num in nums:
        if num is 1 :
            ones.append(num)
        elif num is 2 :
            twos.append(num)
        else :
            threes.append(num)
    return ones + twos + threes

# print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]
print(sortNums([3, 3, 2, 1, 3, 2, 1]))
