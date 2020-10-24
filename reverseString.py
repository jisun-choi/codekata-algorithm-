def reverseString(str):
    new_str = ''
    while len(str) > 0:
        new_str += str[-1]
        str = str[:-1]
    return new_str
print(reverseString('hello'))
#model solution 

def reverseString(str):
      if len(str) == 0:
    return str
  else:
    return reverseString(str[1:]) + str[0]
