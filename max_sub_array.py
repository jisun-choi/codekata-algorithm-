def maxSubArray(nums):
    max_so_far = curr_so_far = -float('inf')
    for i in range(len(nums)):
        curr_so_far += nums[i] # Add curr number
        print('1',curr_so_far)
        curr_so_far = max(curr_so_far, nums[i]) # Check if should abandon accumulated value so far if it's a burden due to negative value accumulated
        #print('2',curr_so_far)
        max_so_far = max(max_so_far, curr_so_far) # Update answer
        print('3',max_so_far)
    return max_so_far
print(maxSubArray([-2,1, 3, 4, -3, 3]))

#model solution
def maxSubArray(nums):
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1] 
            print(nums)
    return max(nums)
  
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

#model solution 
def maxSubArray(A):
    if not A:
        return 0

    curSum = maxSum = A[0]
    for num in A[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum
        