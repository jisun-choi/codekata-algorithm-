def is_valid(string):
	left = ['(', '{', '[']
	right = [')', '}', ']']
	stack = []
    
	for letter in string:
		if letter in left:
			stack.append(letter)
		elif letter in right:
			if len(stack) <= 0:
				return False
			if left.index(stack.pop()) != right.index(letter):
				return False
	return len(stack) == 0