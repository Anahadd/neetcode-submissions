class Solution:

    def helper(self, s: str) -> str:
        text = ""

        for char in s.lower():
            if char.isascii() and char.isalnum():
                text += char

        return text

    def isPalindrome(self, s: str) -> bool:
        checkPalindrome = self.helper(s)

        L = 0
        R = len(checkPalindrome) - 1

        while L < R:
            if checkPalindrome[L] != checkPalindrome[R]:
                return False

            L += 1
            R -= 1

        return True