class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = {}

        for i, n in enumerate(numbers):
            find = target - n
            if find in x:
                return [x[find], i]

            x[n] = i
            
            