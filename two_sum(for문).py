def two_sum(nums, target):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]

print(two_sum([4,9,11,14], 13))
print(two_sum([3,2,11,4], 13))

#배열 안의 수를 모두 비교하는 경우 
def two_sum(numbers, target):
    for index1 in range(len(numbers)):
        for index2 in range(len(numbers)):
            if index1 != index2:
                if numbers[index1] + numbers[index2] == target:
                    return index1, index2

numbers = [4, 9, 11, 14]
target = 13

print(list(two_sum(numbers, target)))
