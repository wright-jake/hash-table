#example input
nums1 = [1,2,2,1], nums2 = [2,2]

#solution
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #sort both lists
        nums1.sort()
        nums2.sort()
        
        #create two pointers to iterate through each list
        first, second = 0, 0
        
        #create empty set
        output = set()
        
        #while pointers are valid
        while first < len(nums1) and second < len(nums2):
            
            #add intersection to output set
            if nums1[first] == nums2[second]:
                output.add(nums1[first])
                
                #increment pointers
                first += 1
                second += 1
            
            #as both lists are sorted we can find the intersection based off the positioning
            elif nums1[first] > nums2[second]:
                second += 1
            else:
                first += 1
        return output
