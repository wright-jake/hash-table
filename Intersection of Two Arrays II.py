#example input
nums1 = [1,2,2,1], nums2 = [2,2]

#solution
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #create hashmap
        hashmap = {}
        
        #create array to store intersection
        res = []
        
        #iterate through nums1
        for num in nums1:
            
            #add each number in nums1 to our hashmap
            hashmap[num] = hashmap.get(num, 0) + 1
            
        #iterate through nums2
        for num in nums2:
            
            #if our number is in the hashmap and positive
            if num in hashmap and hashmap[num] > 0:
                
                #add the number to the hashmap
                res.append(num)
                
                #reduce the count of times that number appears in the list
                hashmap[num] -= 1
        
        #return intersection
        return res
