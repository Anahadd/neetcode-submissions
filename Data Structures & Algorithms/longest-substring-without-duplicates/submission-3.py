class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashMap = {}

        count = 0
        max_count = 0
        start = 0
        for i in range(0, len(s)): 

            if s[i] not in hashMap or hashMap[s[i]] < start: 
                hashMap[s[i]] = i
                count = i - start + 1
            else: 
                start = hashMap[s[i]] + 1
                hashMap[s[i]] = i
                count = i - start + 1
            
            if count > max_count:
                max_count = count 

        return max_count