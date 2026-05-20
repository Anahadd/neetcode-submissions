class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        L = 0 
        countOnes = 0 
        length = 0 
        
        # 1 0 1 1 0 
        # L = 0, R = 0 -> length = 1 since nums[0] = 1
        # L = 0, R = 1 (2 - 1 = 1) L = 1, length = 1 
        # L = 1, R = 2 (countones = 2) 2 - 1 + 1 = 2 -2 = 0 length = 2 
        # L = 1, R = 3 (countones = 3) 0 length = 3 
        # L = 1, R = 4 (countones = 3) 4 - 1 + 1 4 - 3 = 1 L = 2 4 - 2 + 1 = 3 
        # length = 4 - 2 + 1 -> 3 so it's 3
        
        for R in range(len(nums)): 

            if nums[R] == 1:
                countOnes += 1 
            
            while (R - L + 1) - countOnes > 1:
                if nums[L] == 1:
                    countOnes -= 1 
                L += 1
            

            length = max(length, R - L + 1)

        return length 

        # 1 0 1 1 0 


             


