def solution(N):
    binary = format(N,'b')
    print(binary)
    count = 0
    count_list = []
    for i in binary:
        if i == '0':
            count += 1
        else:
            count_list.append(count)
            count = 0 
    return max(count_list)

print(solution(133))