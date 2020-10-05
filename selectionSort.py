def selectionSort(nums):
    for stand in range(len(nums) - 1):
        lowest = stand
        for index in range(stand + 1, len(nums)):
            if nums[lowest] > nums[index]:
                lowest = index
        nums[lowest], nums[stand] = nums[stand], nums[lowest]
    return nums