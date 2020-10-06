# def bubbleSort(arr):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#             #continue
#     return arr


#model solution 
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
    # 마지막 i번째는 이미 큰 수로 정렬된 상태니까 그 전까지
        for j in range(0, n-i-1):
            print(j, n-i-1)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 3, 1, 6, 2, 8, 0, 4]
print(bubbleSort(arr))