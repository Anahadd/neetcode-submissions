class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        L = 0
        freqZ = 0
        maxOnes = 0 
        for R in range(len(nums)):

            if nums[R] == 0:
                freqZ += 1

            while freqZ > k:
                if nums[L] == 0:
                    freqZ -= 1
                L += 1
            
            maxOnes = max(maxOnes, R - L + 1)
            
        return maxOnes


            
