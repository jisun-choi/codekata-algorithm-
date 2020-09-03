def get_len_of_str(string):
    index_list = []
    for i in range(len(string)-1):
            if string[i] == string[i+1]:
                index_list.append(i)    
    print(index_list) 
    while len(index_list)>0: 
        start = []
        for i in range(len(index_list)-1):
            if index_list[i] != index_list[i+1]:
                start.append(i)
        print(start)
        x = index_list[-1]
        string = string[x+1:]
        return len(string)
    return len(string)
print(get_len_of_str('abcdd'))
# print(get_len_of_str('abcabcbb'))

#model solution 
def get_len_of_str(string):
    x=[]
    j=''
    for i in string:
        if i in j:
            x.append(len(j))
            j=i
        else:
            j=j+i
            x.append(len(j))
        return max(x)

print(get_len_of_str('abcabcabc'))


