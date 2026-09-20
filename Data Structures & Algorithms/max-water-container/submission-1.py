class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we want to optimize |index2 - index1| and max(index2, index1)
        # this will yield the greatest area
        # 2 pointer 

        L = 0 
        R = len(heights) - 1
        area = 0

        # 0, 1, 2, 3, 4, 5

        while L < R:

            width = R - L 
            height = min(heights[R], heights[L])
            area = max(area, width * height)

            if heights[R] < heights[L]:
                R -= 1 
            else: 
                L += 1
        
        return area

