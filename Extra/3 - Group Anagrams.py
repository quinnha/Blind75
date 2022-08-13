# create dic of L-value = sorted_str - str, and append to dic if exists
def groupAnagrams(strs):

    out = []
    d = {}
    
    for i in strs:
        str_s = "".join(sorted(i))
        if not (str_s in d):  
            d[str_s] = [i] 
        else:
            d[str_s].append(i)
    
    for key in d:
        out.append(d[key])

    return out


print (groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print (groupAnagrams(["a"]))
