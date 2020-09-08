def more_than_half(nums):
    new_nums=list(set(nums))
    counts = []
    for i in new_nums:
        counts.append(nums.count(i))

    for j in counts:
        if j > (len(nums)/2):
            index = counts.index(j)
            return new_nums[index]

nums = [1]
print(more_than_half(nums))

def more_than_half(nums):
    	majority_count = len(nums)//2
	for num in nums:
		count = sum(1 for elem in nums if elem == num)
		if count > majority_count:
			return num


#아니면 hashmap
# import collections

# def more_than_half(nums):
# 	counts = collections.Counter(nums)
# 	return max(counts.keys(), key=counts.get)

#아니면 sort
# def more_than_half(nums):
# 	nums.sort()
# 	return nums[len(nums)//2]



    