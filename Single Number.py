#example input
nums = [4,1,2,1,2]

#solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #create a hashset
        hashset = set()
        
        #iterate through the list
        for n in nums:
            
            #check to see if n is in hashset
            if n in hashset:
                
                #if it is remove it as this will be a duplicate
                hashset.remove(n)
            
            else:
                #if not in hashset, add n to hashset and check next number in array
                hashset.add(n)
        
        #after iterating through the list, there will be one number left (the one that doesn't appear twice)
        return hashset.pop()
