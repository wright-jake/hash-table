#example input
nums = [1,2,3,1]

#solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create a hashset where we will store all checked values
        hashset = set()
        
        #iterate through the array
        for n in nums:
            
            #check to see if n is in hashset (where all previous non-duplicate integers are stored)
            if n in hashset:
                return True
            
            #if not in hashset, add n to hashset and check next number in array
            hashset.add(n)
            
        #if we iterate through entire array and can't find n in nums then that means no duplicates
        return False
