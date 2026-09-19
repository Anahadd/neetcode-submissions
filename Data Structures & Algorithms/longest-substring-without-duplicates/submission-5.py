'''
Sliding Window + Hashmap 

Window is valid -> 
* if there's no duplicate, we can use a set / hashmap for this. 
* if the char exists within the hashmap, we move L += 1 otherwise 
* we increase length, then we set length = max(length, curr)

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        L = 0 
        length = 0 
        setChar = set()

        for R in range(len(s)):

            while s[R] in setChar: 

                setChar.remove(s[L])
                L += 1

            if s[R] not in setChar: 
                setChar.add(s[R])

            length = max(length, R - L + 1)

        return length 