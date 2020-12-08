def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        modified_arr = array[commands[i][0] - 1 : commands[i][1]]
        final_arr = sorted(modified_arr)
        ans = final_arr[commands[i][2] - 1]
        answer.append(ans)
    return answer


# 모델답안
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(list(sorted(array[i - 1 : j]))[k - 1])
    return answer


# 모델답안2
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1 : x[1]])[x[2] - 1], commands))

