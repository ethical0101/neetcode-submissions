class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1

        maxSum = 0

        while start < end:
            minimum = min(heights[start], heights[end])

            sum = minimum * (end - start)

            maxSum = max(maxSum, sum)

            if heights[start] < heights[end]:
                start+=1
            else:
                end-=1
        
        return maxSum