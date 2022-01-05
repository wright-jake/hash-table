#example input
s = "egg", t = "add"

#solution
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #if the strings are not equal length then they cannot be isomorphic
        if len(s)!=len(t): 
            return False
        
        #create hashmap
        hashmap = {}
        
        #iterate through string
        for i in range(len(s)):
            
            #check if character from first string is in hashmap 
            if s[i] not in hashmap.keys():
                
                #check if character from second string is in hashmap 
                if t[i] not in hashmap.values():
                    
                    #assign mapping
                    hashmap[s[i]] = t[i]
                
                #mapping is invalid so cannot be isomorphic
                else:
                    return False
            
            #if previous mapping we have set does not hold then cannot be isomorphic
            elif hashmap[s[i]] != t[i]:
                    return False
        
        return True
