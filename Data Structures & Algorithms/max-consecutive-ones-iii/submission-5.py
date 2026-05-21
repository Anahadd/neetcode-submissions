class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        L = 0 
        freqZero = 0 
        length = 0 
        arr_len = len(nums)

        for R in range(arr_len):

            if nums[R] == 0:
                freqZero += 1
            
            while freqZero > k:

                if nums[L] == 0:
                    freqZero -= 1
                L += 1
            
            length = max(length, R - L + 1)
        
        return length 
        