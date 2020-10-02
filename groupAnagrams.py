def groupAnagrams(strs):
    counter = {}
    for s in strs:
        key = ''.join(sorted(s))
        print('key', key)
 
        if key not in counter:
            counter[key] = []
            print(counter)
        # 그리고 문자열을 해당 key에 할당해줍니다.
        counter[key].append(s)
    result = []
    for key in counter:
        result.append(counter[key])
     
    return result


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
