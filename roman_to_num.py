def roman_to_num(string):
        roman =0
        symbol = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
}
        for i in string:
                roman += symbol[i]
        
        if 'CD' in string:
                roman = roman - 200
        if 'CM' in string:
                roman = roman - 200
        if 'XL' in string:
                roman -= 20 
        if 'XC' in string:
                roman -= 20 
        if 'IV' in string:
                roman -= 2 
        if 'IX' in string:
                roman -= 2 
                
        return roman

print(roman_to_num('LVIII'))

# string = 'MCMXCIV'
# if ('CD' and 'CM') in string:
#         print(1)
# else: 
#         print(2)