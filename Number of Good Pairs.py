#example input
nums = [1,2,3,1,1,3]

#solution
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        #create hashmap
        hashmap = {}
        
        #create count to store number of good pairs
        res = 0
        
        #iterate through nums
        for num in nums:
            
            #if number already exisits in hashmap, add the number of pairs to the count and increment the hashmap value
            if num in hashmap:
                res += hashmap[num]
                hashmap[num] += 1
            
            #if not, just add the number to the hashmap
            else:
                hashmap[num] = 1
        
        #return count of good pairs
        return res
