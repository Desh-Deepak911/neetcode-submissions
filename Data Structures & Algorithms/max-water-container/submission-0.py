class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        area = (r - l) * min(heights[l], heights[r])
        res = area

        while l < r:
            if heights[l] <= heights[r]:
                l += 1 
            elif heights[l] > heights[r]:
                r -= 1
            area = (r - l) * min(heights[l], heights[r])
            res = max(area, res)
        
        return res


        