#example input
s = "abcabcbb"

#solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create hashset where we can check for duplicates
        char_set = set()
        
        #create somewhere for us to store our substring length
        res = 0
        
        #initialise two pointers
        left = 0
        
        for right in range(len(s)):
            
            #if right pointer letter is already in hashset (is a duplicate)
            while s[right] in char_set:
                
                #we will remove left pointer letter
                char_set.remove(s[left])
                
                #and then increment left pointer by 1
                left += 1
                
                #we will keep removing letters from the left side until the substring contains no duplicates
                
            #we then need to add the right pointer letter to the hashset   
            char_set.add(s[right])
            
            #the longest (maximum) substring
            res = max(res, right-left+1)
        
        #returns the longest substring
        return res
