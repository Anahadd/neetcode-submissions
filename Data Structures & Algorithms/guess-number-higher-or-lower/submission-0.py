# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Binary Search O(log n)

# [1, 2, 3, 4, 5, 6]


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0 
        right = n 

        while left <= right: 
            mid = (left + right) // 2 

            if guess(mid) < 0:
                right = mid - 1 
            elif guess(mid) > 0:
                left = mid + 1
            else:
                return mid 

        return -1 