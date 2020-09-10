def top_k(nums, k):
    new_nums = list(set(nums))
    count_list = {}
    for num in new_nums:
        count_list[num] = nums.count(num)
    sorted_list = sorted(count_list.items(), key=lambda x:x[1], reverse=True)
    answer = []
    for i in range(k):
        answer.append(sorted_list[i][0])
    return answer

#model solution 
def top_k(nums, k):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    bucket = [[] for _ in range(len(nums)+1)]
    for n, freq in count.items():
        bucket[freq].append(n)
    ret = []
    for n_list in bucket[::-1]:
        if n_list:
            ret.extend(n_list)
            if len(ret) == k:
                return ret

nums = [1,1,2,2,2,2,3,3,3]
k = 2

print(top_k(nums, k))
