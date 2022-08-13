# O(n) time! make 2 dicts and comapre the two, python will return true regardless of key/value order :) 

def isAnagram(s,t):
    s_set = set(s)
    t_set = set(t)
    dic_s = {}
    dic_t = {}
    for i in s_set:
        dic_s[i] = s.count(i)
        
    for i in t_set:
        dic_t[i] = t.count(i)

    return (dic_s == dic_t) 

print(isAnagram("a", "ab"))


# d = {"a": 3, "b": 4}
# d1 = {"b":4}
# print (d == d1)