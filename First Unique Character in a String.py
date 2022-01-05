#example input
s = "leetcode"

#solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        #create hashmap
        hashmap = {}
        
        #iterate through string
        for i in range(len(s)):
            
            #if letter is not in hashmap, add it in and give it the value of its' index
            if s[i] not in hashmap:
                hashmap[s[i]] = i
            
            #if it is in hashmap, set the mapping as false as this character is repeated
            else:
                hashmap[s[i]] = False
        
        #we want to return the index of the first unique character/the first character where its' mapping is not false
        for k, v in hashmap.items():
            if v is not False:
                return v
        
        #if no unique characters, return -1
        return -1
