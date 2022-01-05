#example input
strs = ["eat","tea","tan","ate","nat","bat"]

#solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #create hashmap
        hashmap = {}
        
        #create array to store the grouped anagrams
        res = []
        
        for word in strs:
            
            #sort each word in the list alphabetically
            sortedword = "".join(sorted(word))
            
            #check for sorted word in hashmap
            if sortedword not in hashmap:
                
                #if not, add to hashmap with sorted word as the key and the anagram as its' value
                hashmap[sortedword] = [word]
            
            #if sorted word is in hashmap
            else:
                
                #add the anagram to the value of that key - this is how we group the anagrams
                hashmap[sortedword].append(word)
            
        #add each group of anagrams to our result array
        for group in hashmap.values():
            res.append(group)

        #return array with anagrams all grouped
        return res
