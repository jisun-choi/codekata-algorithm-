def search(numbs, target):
    left, right = 0, len(nums) - 1
    while left < right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        else:
            left = pivot + 1
    return -1 


