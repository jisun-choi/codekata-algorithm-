def getMap(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin_str = bin(arr1[i] | arr2[i])[2:]
        print(bin_str)
        answer.append(('0' * (n-len(bin_str)) + bin_str).replace('1', '#').replace('0'," "))
    return answer

arr1=[9,20,28,18,11]
arr2=[30,1,21,17,28]
print(getMap(5, arr1,arr2))

#model solution 
def getMap(n, arr1, arr2):
      return [format(arr1[i] | arr2[i], f'0{n}b').replace('1', '#').replace('0', ' ') for i in range(n)]
