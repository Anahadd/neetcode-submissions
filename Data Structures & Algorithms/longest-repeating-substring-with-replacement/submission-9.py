class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 

        L = 0 
        hashmap = {}
        count = 0 
        
        for R in range(len(s)): 

            if s[R] not in hashmap:
                hashmap[s[R]] = 1
            else:
                hashmap[s[R]] += 1

            while (R-L+1) - max(hashmap.values()) > k:
                hashmap[s[L]] -= 1
                L += 1
            
            count = max(count, R - L + 1)

        return count 
            



            


            











            
            


        

        