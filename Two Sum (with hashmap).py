#example input
nums = [2,7,11,15], target = 9

#solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hashmap where we will store the index of a number:value of that number
        hashmap = {}
        
        #enumerate allows us to return the index as i and then the value of the number as n
        for i, n in enumerate(nums):
            
            #calculate the difference between the target and n, if the difference is in the hashmap then we have found a match
            diff = target - n
            
            if diff in hashmap:
                
                #if difference is in hashmap we want to return the index of both numbers that sum to make the target
                return [hashmap[diff], i]
            
            #if not in the hashmap add n to the hashmap and then loop back through
            hashmap[n] = i
