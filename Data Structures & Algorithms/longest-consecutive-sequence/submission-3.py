class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = set(nums)

        long = 0;

        for num in nums:
            if num - 1 not in ans:
                length = 1

                while num + length in ans:
                    length += 1    
                long = max(long, length)

        return long