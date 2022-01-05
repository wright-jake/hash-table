#example input
n = 19

#solution
class Solution:
    def isHappy(self, n: int) -> bool:
        #create hashset
        seen = set()
        
        #check if number is in hashset
        while n not in seen:
            
            #add n to hashset
            seen.add(n)
            
            #initialise sum of squares
            sum = 0
            
            while n > 0:
                
                #square last digit
                sum += (n % 10) * (n % 10)
                
                #iterate through other digits
                n = n // 10
            
            #if sum is 1 then it is a happy number
            if sum == 1:
                return True
            
            #we keep looping through with the new sum of the squares until n is 0
            n = sum
            
        return False
