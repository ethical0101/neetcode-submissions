class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0] * len(nums)
        r = [0] * len(nums)
        # r = []

        result = [0] * len(nums)

        l[0] =1
        r[len(nums)-1] = 1

        for i in range(1, len(nums)):
            l[i] = l[i-1]*nums[i-1]

        for j in range(len(nums)-2,-1, -1):
            r[j] = r[j+1]*nums[j+1]
        
        for k in range(len(nums)):
            result[k] = l[k]*r[k]
        

        return result