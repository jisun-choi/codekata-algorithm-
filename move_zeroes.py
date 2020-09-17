def moveZeroes(nums):
    count = 0
    while 0 in nums:
        if 0 in nums:
            nums.remove(0)
            count += 1
    for add in range(count):
        nums.append(0)
    return nums

def moveZeroes(nums):
      last0 = 0
  
  for i in range(0, len(nums)):
    if nums[i] != 0:
      nums[i], nums[last0] = nums[last0], nums[i]
      last0 += 1
      
  return nums