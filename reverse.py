#내 답안
def reverse(x):
    if x >= 0:
        r = str(x)
        reversed_num = []
        for i in reversed(r):
            reversed_num.append(i)
        return int(''.join(reversed_num))
    else: 
        x = -(x)
        r = str(x)
        reversed_num = ['-']
        for i in reversed(r):
            reversed_num.append(i)
        return int(''.join(reversed_num))

print(reverse(-1234))

#model solution 
def reverse(number):
    	string = str(number)
	if string[0] == '-':
		string = string[::-1]
		new_string = string[-1]+string[:-1]
		return int(new_string)
	string = string[::-1]
	return int(string)