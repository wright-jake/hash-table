#example input
s = "anagram", t = "nagaram"

#solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if length of strings s and t isn't the same then they cannot be anagrams of each other
        if len(s) != len(t):
            return False
        
        #create hashmaps to count how many times each letter occurs in each string
        countS = {}
        countT = {}
        
        #we will iterate through the length of the string
        for i in range(len(s)):
            
            #each time we see a letter add 1 to the count, return 0 if not
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        #check to see if count of distinct letters in each hasmap equals out
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
            
        return True
