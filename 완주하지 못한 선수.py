from collections import Counter


def solution(participant, completion):
    sorted_participant = set(participant)
    if len(sorted_participant) == len(completion):
        duplicated = Counter(participant)
        for i in duplicated:
            if duplicated[i] != 1:
                answer = i
                return answer
    else:
        for one in participant:
            if one not in completion:
                answer = one
                return answer


# 모델답안
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
