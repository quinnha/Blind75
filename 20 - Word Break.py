# time limit exceed >:(, O(2^n) runtime, brute force
def wordBreak(s, wordDict):
    print (s)

    if s in wordDict: return True #base case

    for words in wordDict:
        if words in s and s.index(words) == 0: 
            if wordBreak(s.replace(words,"", 1) , wordDict): return True

    return False 

#better word break
# idea is to check at every index, if the word can be separated, and go bottome up
def wordBreak(self, s, wordDict):

        dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
                    
        return dp[-1] #return the last one because if its True, we've made it up to string (dp[len(s)])!


s = "ccbb"
dic = ["bc","cb"]

print(wordBreak(s, dic))