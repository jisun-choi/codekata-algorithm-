def complexNumberMultiply(a, b):
  a1, a2 = map(int, a[:-1].split('+'))
  b1, b2 = map(int, b[:-1].split('+'))
  return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)

# def complexNumberMultiply(a, b):
#     firstArr = a[:-1].split('+')
#     print(firstArr)
#     a1 = int(firstArr[0])
#     a2 = int(firstArr[1])

#     secondArr = b[:-1].split('+')
#     b1 = int(secondArr[0])
#     b2 = int(secondArr[1])

#     return f'{a1 * b1 - a2 * b2}+{a1 * b2 + a2 * b1}i'

print(complexNumberMultiply("1+1i", "1+1i"))