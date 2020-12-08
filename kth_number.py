def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        modified_arr = array[commands[i][0] - 1 : commands[i][1]]
        final_arr = sorted(modified_arr)
        # print(1)
        # print(sorted(modified_arr))
        # print(final_arr, 1)
        # print(commands[i][2])
        print(final_arr)
        print(final_arr[commands[i][2] - 1])
        ans = final_arr[commands[i][2] - 1]
        # print(2)
        answer.append(ans)
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
