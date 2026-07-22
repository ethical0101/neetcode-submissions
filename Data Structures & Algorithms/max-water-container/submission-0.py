class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j and j > i: 
                    small = heights[i]
                    if heights[i] > heights[j]:
                        small = heights[j]
                    width = j - i
                    ans = small * width
                    if res <= ans:
                        res = ans
        return res
                    