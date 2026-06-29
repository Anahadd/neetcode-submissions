class Solution:
    def isValid(self, s: str) -> bool:

        hashmap = {
            '(': ')', 
            '{': '}', 
            '[': ']'
        }
        stack = []
        for char in s:
            if char in hashmap: 
                stack.append(char)
            else: 
                if not stack:
                    return False 
                if hashmap[stack[-1]] != char:
                    return False 
                stack.pop()

        if not stack:
            return True 
        else:
            return False 