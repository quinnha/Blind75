# time limit exceed >:(
def wordBreak(s, wordDict):
    print (s)

    if s in wordDict: return True #base case

    for words in wordDict:
        if words in s and s.index(words) == 0: 
            if wordBreak(s.replace(words,"", 1) , wordDict): return True

    return False 


s = "ccbb"
dic = ["bc","cb"]

print(wordBreak(s, dic))


# td = ["hello", "pog"]

# s = "hellopwog"

# print(s[len(td[0]):])

# print(s.replace(dic[1], ""))

# t = "bb"
# print(t.replace("b", "1", 1))