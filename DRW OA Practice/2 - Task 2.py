# Minimum Deletions to Make Character Frequencies Unique - https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/
import collections

def solution(A):
    S = collections.Counter(A)
    count= 0
    unique = set() 
    for char, freq in S.items():
        while freq >0 and freq in unique:
            freq-=1
            count+=1      
        unique.add(freq)
    return count
